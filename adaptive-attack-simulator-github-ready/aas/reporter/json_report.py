
import os, json, time
def save_json(report_dir, target, findings):
    os.makedirs(report_dir, exist_ok=True)
    fname = os.path.join(report_dir, f"report_{target.replace('://','_').replace('/','_')}_{int(time.time())}.json")
    with open(fname,'w',encoding='utf-8') as f:
        json.dump({'target': target, 'ts': int(time.time()), 'findings': findings}, f, indent=2)
    return fname
