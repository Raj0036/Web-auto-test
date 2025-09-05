
from ..plugins.base import PluginBase
import httpx
class XSSCheck(PluginBase):
    def run(self):
        findings = []
        payloads = ["<script>alert(1)</script>", '"\'><img src=x onerror=alert(1)>']
        for p in payloads:
            try:
                r = httpx.get(self.target, params={'q': p}, timeout=10.0)
                if p in r.text:
                    findings.append({'name':'Reflected XSS','details':{'payload':p,'url':str(r.url)}})
            except Exception as e:
                findings.append({'name':'XSS Check Error','details':{'error':str(e)}})
        return findings
