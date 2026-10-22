import copy
from fractions import Fraction
import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from score_assessment import assess, load, profile, GATES

BASE=Path(__file__).resolve().parents[1]
class ScoringTests(unittest.TestCase):
 def test_worked_evidence_case(self):
  d=load(BASE/'examples/willow_worked_case/assessment.json')
  r=assess(d)
  self.assertEqual(r['organisation']['score_sum'],73)
  self.assertEqual(r['organisation']['index_percent'],48.7)
  self.assertEqual(r['organisation']['capability_profile'],'Partially established')
  self.assertEqual(r['organisation']['coverage_percent'],100)
  self.assertEqual(r['gates']['G4']['red_questions'],['Q21'])
  for g in ('G1','G2','G3'):self.assertEqual(r['gates'][g]['status'],'amber')
  self.assertEqual(len(d['evidence_register']),30)
 def setUp(self): self.data=load(BASE/'examples/fictional_assessment.json')
 def row(self,q,case=False):
  rows=self.data['use_case']['gate_responses'] if case else self.data['organisation_responses']
  return next(r for r in rows if r['question_id']==q)
 def score(self,q,s,case=False):
  r=self.row(q,case);r.update(state='scored',score=s,evidence_mode='confirmed_absence' if s==0 else 'exercise')
 def unknown(self,q,case=False):
  r=self.row(q,case);r['state']='unknown';r.pop('score',None);r.pop('evidence_mode',None)
 def test_baseline(self):
  r=assess(self.data);self.assertEqual(r['organisation']['index_percent'],60);self.assertEqual(r['gate_summary'],'prerequisites_evidenced')
 def test_each_gate_red(self):
  for g,ids in GATES.items():
   with self.subTest(g=g):
    d=copy.deepcopy(self.data);r=next(r for r in d['use_case']['gate_responses'] if r['question_id']==ids[0]);r['score']=1
    self.assertEqual(assess(d)['gates'][g]['status'],'red')
 def test_every_gate_item(self):
  for ids in GATES.values():
   for q in ids:
    with self.subTest(q=q):
     d=copy.deepcopy(self.data);next(r for r in d['use_case']['gate_responses'] if r['question_id']==q)['score']=2
     self.assertEqual(assess(d)['gate_summary'],'amber')
 def test_high_score_no_override(self):
  for r in self.data['organisation_responses']:r['score']=5
  self.score('Q21',0);self.score('Q21',0,True)
  r=assess(self.data);self.assertEqual(r['organisation']['index_percent'],96.7);self.assertEqual(r['gate_summary'],'red')
 def test_org_unknown(self):
  self.unknown('Q29');r=assess(self.data);self.assertIsNone(r['organisation']['index_percent']);self.assertEqual(r['gate_summary'],'prerequisites_evidenced')
 def test_case_independent(self):
  self.unknown('Q30',True);r=assess(self.data);self.assertEqual(r['organisation']['index_percent'],60);self.assertEqual(r['gate_summary'],'unresolved')
 def test_red_beats_unknown(self):
  self.score('Q19',1,True);self.unknown('Q30',True);r=assess(self.data);self.assertEqual(r['gate_summary'],'red');self.assertIn('Q30',r['gates']['G4']['unresolved_questions'])
 def test_unknown_beats_amber(self):
  self.score('Q19',2,True);self.unknown('Q30',True);self.assertEqual(assess(self.data)['gate_summary'],'unresolved')
 def test_omitted_question(self):
  self.data['organisation_responses'].pop();self.assertEqual(assess(self.data)['organisation']['scored_count'],29)
 def test_omitted_gate(self):
  self.data['use_case']['gate_responses'].pop();self.assertEqual(assess(self.data)['gate_summary'],'unresolved')
 def test_invalid_scores(self):
  for value in (-1,6,2.5,True,'3',None):
   with self.subTest(value=value):
    self.row('Q1')['score']=value
    with self.assertRaises(ValueError):assess(self.data)
 def test_duplicate(self):
  self.data['organisation_responses'].append(copy.deepcopy(self.row('Q1')))
  with self.assertRaises(ValueError):assess(self.data)
 def test_unexpected_id(self):
  self.row('Q1')['question_id']='Q31'
  with self.assertRaises(ValueError):assess(self.data)
 def test_na_rejected(self):
  self.row('Q1')['state']='not_applicable'
  with self.assertRaises(ValueError):assess(self.data)
 def test_evidence_required(self):
  self.row('Q1')['evidence_ids']=[]
  with self.assertRaises(ValueError):assess(self.data)
 def test_unknown_no_score(self):
  self.row('Q1')['state']='unknown'
  with self.assertRaises(ValueError):assess(self.data)
 def test_version(self):
  self.data['metadata']['methodology_version']='other'
  with self.assertRaises(ValueError):assess(self.data)
 def test_future_evidence(self):
  self.data['evidence_register']['E01']['date']='2099-01-01'
  with self.assertRaises(ValueError):assess(self.data)
 def test_band_boundaries_and_rounding(self):
  names=['Foundational gaps','Early development','Partially established','Established capabilities']
  for boundary,name in zip((20,40,60,80),names):
   self.assertEqual(profile(Fraction(boundary)),name)
   self.assertNotEqual(profile(Fraction(boundary)+Fraction(1,1000)),name)
 def test_duplicate_json_key(self):
  from score_assessment import unique_object
  with self.assertRaises(ValueError):json.loads('{"a":1,"a":2}',object_pairs_hook=unique_object)
 def test_zero_mode(self):
  self.row('Q1')['score']=0
  with self.assertRaises(ValueError):assess(self.data)
if __name__=='__main__':unittest.main()
