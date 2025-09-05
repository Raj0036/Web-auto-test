
from ..plugins.base import PluginBase
import httpx
class CORSCheck(PluginBase):
    def run(self):
        findings = []
        try:
            r = httpx.get(self.target, headers={'Origin':'http://evil.com'}, timeout=10.0)
            acao = r.headers.get('access-control-allow-origin','')
            if acao == '*' or 'evil.com' in acao:
                findings.append({'name':'Overly Permissive CORS','details':{'acao':acao}})
        except Exception as e:
            findings.append({'name':'CORS Check Error','details':{'error':str(e)}})
        return findings
