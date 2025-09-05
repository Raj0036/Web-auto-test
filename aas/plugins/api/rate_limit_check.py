
from aas.plugins.base import PluginBase
import httpx
class RateLimitCheck(PluginBase):
    def run(self):
        findings = []
        try:
            for i in range(5):
                httpx.get(self.target, timeout=6.0)
            r = httpx.get(self.target, timeout=6.0)
            if r.status_code==429:
                findings.append({'name':'Rate Limit Detected','details':{'status':429}})
        except Exception as e:
            findings.append({'name':'Rate Limit Error','details':{'error':str(e)}})
        return findings
