
class PluginBase:
    def __init__(self, target, config=None):
        self.target = target
        self.config = config or {}
    def run(self):
        raise NotImplementedError
