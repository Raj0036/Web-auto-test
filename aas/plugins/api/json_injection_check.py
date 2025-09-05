
from ..plugins.base import PluginBase
import httpx
class JSONInjectionCheck(PluginBase):
    def run(self):
        findings = []
        try:
            headers = {'Content-Type':'application/json'}
            payload = {'name':'\"; alert(1); //','email':'test@example.com'}
            r = httpx.post(self.target + '/api/users', json=payload, headers=headers, timeout=8.0)
            if r.status_code in (200,201):
                findings.append({'name':'JSON Endpoint Response','details':{'status':r.status_code,'url':str(r.url)}})
        except Exception as e:
            findings.append({'name':'JSON Injection Error','details':{'error':str(e)}})
        return findings
