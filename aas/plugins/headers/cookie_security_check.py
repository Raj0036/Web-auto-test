
from aas.plugins.base import PluginBase
import httpx
class CookieSecurityCheck(PluginBase):
    def run(self):
        findings = []
        try:
            r = httpx.get(self.target, timeout=10.0)
            cookies = r.cookies.jar
            for c in cookies:
                flags = {'secure': getattr(c,'secure',False), 'httponly': 'httponly' in getattr(c,'_rest',{})}
                if not flags['secure'] or not flags['httponly']:
                    findings.append({'name':'Insecure Cookie','details':{'cookie':c.name,'flags':flags}})
        except Exception as e:
            findings.append({'name':'Cookie Check Error','details':{'error':str(e)}})
        return findings
