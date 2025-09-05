
from ..plugins.base import PluginBase
import httpx
class ClickjackingCheck(PluginBase):
    def run(self):
        findings = []
        try:
            r = httpx.get(self.target, timeout=10.0)
            xfo = r.headers.get('x-frame-options','')
            csp = r.headers.get('content-security-policy','')
            if not xfo and 'frame-ancestors' not in csp:
                findings.append({'name':'Clickjacking Protection Missing','details':{'x-frame-options':xfo,'csp':csp}})
        except Exception as e:
            findings.append({'name':'Clickjacking Check Error','details':{'error':str(e)}})
        return findings
