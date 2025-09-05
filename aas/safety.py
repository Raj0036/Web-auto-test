
import os, time
class Safety:
    def __init__(self, token=None):
        self.config = {'per_host_delay': 1.0, 'concurrency': 4, 'report_dir': 'reports'}
        self.token = token or os.getenv('AAS_AUTH_TOKEN')
    def is_authorized(self):
        return bool(self.token) and len(self.token) > 8
    def before_probe(self, host):
        time.sleep(self.config.get('per_host_delay', 1.0))
