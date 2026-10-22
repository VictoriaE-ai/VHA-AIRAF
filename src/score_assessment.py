"""VHA-AIRAF development calculator. Standard library only; no deployment approval."""
import argparse
from datetime import date
from fractions import Fraction
import json
from pathlib import Path

VERSION = '0.1.0'
METHOD = '1.2-consolidated-draft'
QUESTION_BANK = '1.2-draft'
QUESTIONS = tuple(f'Q{i}' for i in range(1, 31))
GATES = {'G1': ('Q4','Q5','Q6'), 'G2': ('Q13','Q14','Q15'),
         'G3': ('Q16','Q17','Q18'), 'G4': ('Q19','Q20','Q21','Q30')}
GATE_IDS = tuple(q for group in GATES.values() for q in group)
PILLARS = ('Leadership and AI Strategy','Data Readiness','Digital Infrastructure',
           'Workforce Capability','Governance and Ethics','Information Governance, Privacy and Cybersecurity',
           'Patient and Care Safety','Person-centred Care','Operational Readiness and Change',
           'Measurement and Continuous Improvement')

def require(condition, message):
    if not condition:
        raise ValueError(message)

def nonempty(value):
    return isinstance(value, str) and bool(value.strip())

def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f'Duplicate JSON key: {key}')
        result[key] = value
    return result

def load(path):
    return json.loads(Path(path).read_text(), object_pairs_hook=unique_object)

def validate_responses(records, allowed, evidence, label):
    require(isinstance(records, list), f'{label}: responses must be a list')
    result = {}
    for row in records:
        require(isinstance(row, dict), f'{label}: response must be an object')
        q = row.get('question_id')
        require(isinstance(q,str) and q in allowed, f'{label}: unexpected question ID {q!r}')
        require(q not in result, f'{label}: duplicate {q}')
        state = row.get('state')
        require(state in ('scored','unknown'), f'{label}/{q}: only scored or unknown supported; N/A disabled')
        require(nonempty(row.get('rationale')), f'{label}/{q}: rationale required')
        ids = row.get('evidence_ids', [])
        require(isinstance(ids,list) and all(isinstance(e,str) and e in evidence for e in ids),
                f'{label}/{q}: unknown or invalid evidence reference')
        if state == 'scored':
            score = row.get('score')
            require(type(score) is int and 0 <= score <= 5, f'{label}/{q}: score must be integer 0–5')
            require(bool(ids), f'{label}/{q}: evidence required')
            mode = row.get('evidence_mode')
            require(mode in ('operational','exercise','mixed','confirmed_absence'), f'{label}/{q}: evidence mode required')
            require((score == 0) == (mode == 'confirmed_absence'), f'{label}/{q}: zero requires confirmed_absence, reserved for zero')
            require(nonempty(row.get('limitations')), f'{label}/{q}: limitations required (state none identified if appropriate)')
        else:
            require('score' not in row and 'evidence_mode' not in row, f'{label}/{q}: unknown cannot contain score or evidence mode')
        result[q] = row
    return result

def profile(index):
    for bound, name in ((20,'Foundational gaps'),(40,'Early development'),
                        (60,'Partially established'),(80,'Established capabilities'),(100,'Strong documented capabilities')):
        if index <= bound:
            return name
    raise ValueError('Index outside range')

def summarize(ids, records):
    scored = [records[q] for q in ids if q in records and records[q]['state']=='scored']
    missing = [q for q in ids if q not in records or records[q]['state']=='unknown']
    total = sum(r['score'] for r in scored)
    complete = not missing
    exact = Fraction(total * 100, 5 * len(ids)) if complete else None
    modes = sorted({r['evidence_mode'] for r in scored})
    return {'status':'complete' if complete else 'assessment_incomplete',
            'scored_count':len(scored),'applicable_count':len(ids),
            'coverage_percent':round(100*len(scored)/len(ids),1),
            'score_sum':total, 'index_percent':round(float(exact),1) if complete else None,
            'capability_profile':profile(exact) if complete else None,
            'unresolved_questions':missing,'evidence_modes':modes,
            'evidence_basis':'mixed evidence' if len(modes)>1 or 'mixed' in modes else (modes[0] if modes else 'none')}

def gate_outcome(ids, records):
    unresolved = [q for q in ids if q not in records or records[q]['state']=='unknown']
    red = [q for q in ids if q in records and records[q]['state']=='scored' and records[q]['score']<=1]
    amber = [q for q in ids if q in records and records[q]['state']=='scored' and records[q]['score']==2]
    status = 'red' if red else 'unresolved' if unresolved else 'amber' if amber else 'prerequisites_evidenced'
    return {'status':status,'red_questions':red,'amber_questions':amber,'unresolved_questions':unresolved}

def assess(data):
    require(isinstance(data,dict), 'Assessment must be an object')
    meta = data.get('metadata')
    require(isinstance(meta,dict), 'metadata required')
    for key in ('organisation','scope','assessor','reviewer','assessment_date','evidence_cutoff_date'):
        require(nonempty(meta.get(key)), f'metadata/{key} required')
    for key in ('assessment_date','evidence_cutoff_date'):
        try:
            date.fromisoformat(meta[key])
        except ValueError:
            raise ValueError(f'metadata/{key}: ISO date required') from None
    require(meta['evidence_cutoff_date']<=meta['assessment_date'], 'Evidence cutoff cannot follow assessment date')
    require(meta.get('methodology_version')==METHOD, 'Unsupported methodology version')
    require(meta.get('question_bank_version')==QUESTION_BANK, 'Unsupported question-bank version')
    evidence = data.get('evidence_register')
    require(isinstance(evidence,dict), 'evidence_register must be an object')
    for key, item in evidence.items():
        require(nonempty(key) and isinstance(item,dict), 'Invalid evidence entry')
        for field in ('description','owner','reference','scope','date','limitations'):
            require(nonempty(item.get(field)), f'Evidence {key}/{field} required')
        try:
            date.fromisoformat(item['date'])
        except ValueError:
            raise ValueError(f'Evidence {key}: ISO date required') from None
        require(item['date']<=meta['evidence_cutoff_date'], f'Evidence {key}: later than cutoff')
    org = validate_responses(data.get('organisation_responses'), QUESTIONS,evidence,'organisation')
    case = data.get('use_case')
    require(isinstance(case,dict), 'use_case required')
    for key in ('id','name','intended_purpose','scope','owner','limitations'):
        require(nonempty(case.get(key)), f'use_case/{key} required')
    scoped = validate_responses(case.get('gate_responses'),GATE_IDS,evidence,'use_case')
    gates = {g:gate_outcome(ids,scoped) for g,ids in GATES.items()}
    priority = ('red','unresolved','amber','prerequisites_evidenced')
    worst = min((v['status'] for v in gates.values()),key=priority.index)
    actions = data.get('actions',[])
    require(isinstance(actions,list), 'actions must be a list')
    for action in actions:
        require(isinstance(action,dict), 'Invalid action')
        for field in ('owner','due_date','acceptance_evidence','description'):
            require(nonempty(action.get(field)), f'action/{field} required')
        try:
            date.fromisoformat(action['due_date'])
        except ValueError:
            raise ValueError('Action due_date must be ISO date') from None
    return {'calculator_version':VERSION,'metadata':meta,'organisation':summarize(QUESTIONS,org),
            'pillars':{name:summarize(QUESTIONS[i*3:i*3+3],org) for i,name in enumerate(PILLARS)},
            'use_case':{k:v for k,v in case.items() if k!='gate_responses'},
            'gates':gates,'gate_summary':worst,'actions':actions,
            'assessment_records':{'organisation_responses':org,'use_case_gate_responses':scoped,'evidence_register':evidence},
            'notice':'Development prototype. Not validated. Evidence adequacy and applicability require human review. No deployment approval is issued.'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    try:
        report = assess(load(args.input))
    except (ValueError, OSError) as exc:
        parser.exit(2, f'Assessment rejected: {exc}\n')
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(f'Created {args.output}; gate summary: {report["gate_summary"]}')

if __name__ == '__main__':
    main()
