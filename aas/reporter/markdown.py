
import os, time, json
def save_md(report_dir, target, findings):
    os.makedirs(report_dir, exist_ok=True)
    fname = os.path.join(report_dir, f"report_{target.replace('://','_').replace('/','_')}_{int(time.time())}.md")
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(f"# AAS Report for {target}\n\n")
        for it in findings:
            f.write('## ' + it.get('name','') + '\n')
            f.write('Details:\n```\n' + json.dumps(it.get('details',{}), indent=2) + '\n```\n\n')
    return fname
