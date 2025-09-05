
from aas.plugins.base import PluginBase
import httpx
class SQLiCheck(PluginBase):
    def run(self):
        findings = []
        payloads = ["' OR '1'='1", "' UNION SELECT NULL-- "]
        for p in payloads:
            try:
                r = httpx.get(self.target, params={'id': p}, timeout=10.0)
                if 'sql' in r.text.lower() or 'syntax' in r.text.lower():
                    findings.append({'name':'Possible SQLi','details':{'payload':p,'url':str(r.url)}})
            except Exception as e:
                findings.append({'name':'SQLi Check Error','details':{'error':str(e)}})
        return findings
