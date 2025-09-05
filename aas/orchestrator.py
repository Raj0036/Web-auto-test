
from .reporter import markdown as mdrep, json_report as jrep
from .store import Store

class Orchestrator:
    def __init__(self, engine, safety):
        self.engine = engine
        self.safety = safety
        self.store = Store()
    def run_all(self):
        results = self.engine.run_all()
        for target, findings in results:
            for f in findings:
                self.store.save(target, f.get('name','unknown'), f.get('details',{}))
            mdrep.save_md(self.safety.config['report_dir'], target, findings)
            jrep.save_json(self.safety.config['report_dir'], target, findings)
