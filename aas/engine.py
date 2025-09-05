
from .plugins.headers.xss_check import XSSCheck
from .plugins.headers.sql_injection_check import SQLiCheck
from .plugins.headers.cookie_security_check import CookieSecurityCheck
from .plugins.headers.open_redirect_check import OpenRedirectCheck
from .plugins.headers.cors_check import CORSCheck
from .plugins.headers.clickjacking_check import ClickjackingCheck
from .plugins.tls.tls_config_check import TLSConfigCheck
from .plugins.api.auth_bypass_check import AuthBypassCheck
from .plugins.api.json_injection_check import JSONInjectionCheck
from .plugins.api.idor_check import IDORCheck
from .plugins.api.rate_limit_check import RateLimitCheck

class Engine:
    def __init__(self, targets, config=None):
        self.targets = targets if isinstance(targets, list) else [targets]
        self.config = config or {}
        self.plugins = [
            XSSCheck, SQLiCheck, CookieSecurityCheck, OpenRedirectCheck,
            CORSCheck, ClickjackingCheck, TLSConfigCheck,
            AuthBypassCheck, JSONInjectionCheck, IDORCheck, RateLimitCheck
        ]

    def run_all(self):
        all_findings = []
        for t in self.targets:
            findings = []
            for P in self.plugins:
                try:
                    p = P(t, config=self.config)
                    r = p.run()
                    if isinstance(r, list):
                        findings.extend(r)
                except Exception as e:
                    findings.append({'name':'Plugin Error','details':{'plugin':P.__name__,'error':str(e)}})
            all_findings.append((t, findings))
        return all_findings
