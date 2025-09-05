
from aas.plugins.base import PluginBase
import httpx
class OpenRedirectCheck(PluginBase):
    def run(self):
        findings = []
        try:
            r = httpx.get(self.target + '/redirect', params={'url':'https://evil.com'}, follow_redirects=False, timeout=10.0)
            if r.status_code in (301,302,303,307,308) and 'evil.com' in r.headers.get('location',''):
                findings.append({'name':'Open Redirect','details':{'url':str(r.url),'location':r.headers.get('location')}})
        except Exception as e:
            findings.append({'name':'Open Redirect Error','details':{'error':str(e)}})
        return findings
