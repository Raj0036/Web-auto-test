
from ..plugins.base import PluginBase
import httpx
class AuthBypassCheck(PluginBase):
    def run(self):
        findings = []
        try:
            r = httpx.get(self.target + '/api/admin', timeout=8.0)
            if r.status_code == 200:
                findings.append({'name':'Auth Bypass Possible','details':{'url':str(r.url),'status':r.status_code}})
        except Exception as e:
            findings.append({'name':'Auth Bypass Error','details':{'error':str(e)}})
        return findings
