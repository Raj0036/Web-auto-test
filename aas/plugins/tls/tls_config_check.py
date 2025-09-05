
from ..plugins.base import PluginBase
import socket, ssl, urllib.parse
class TLSConfigCheck(PluginBase):
    def run(self):
        findings = []
        try:
            u = urllib.parse.urlparse(self.target)
            host = u.hostname or self.target
            port = u.port or 443
            ctx = ssl.create_default_context()
            with socket.create_connection((host, port), timeout=6) as s:
                with ctx.wrap_socket(s, server_hostname=host) as ss:
                    proto = ss.version()
                    findings.append({'name':'TLS Info','details':{'protocol':proto}})
        except Exception as e:
            findings.append({'name':'TLS Check Error','details':{'error':str(e)}})
        return findings
