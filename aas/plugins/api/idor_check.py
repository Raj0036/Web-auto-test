
from aas.plugins.base import PluginBase
import httpx
class IDORCheck(PluginBase):
    def run(self):
        findings = []
        try:
            r1 = httpx.get(self.target + '/api/orders/1', timeout=6.0)
            r2 = httpx.get(self.target + '/api/orders/2', timeout=6.0)
            if r1.status_code==200 and r2.status_code==200 and r1.text!=r2.text:
                findings.append({'name':'IDOR Potential','details':{'urls':[str(r1.url),str(r2.url)]}})
        except Exception as e:
            findings.append({'name':'IDOR Check Error','details':{'error':str(e)}})
        return findings
