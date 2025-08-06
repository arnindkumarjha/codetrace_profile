class Profiler:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.events = []

    def start(self):
        if self.start_time is not None:
            raise RuntimeError("Profiler is already running.")
        self.start_time = self._current_time()
        self.events.append(("start", self.start_time))

    def stop(self):
        if self.start_time is None:
            raise RuntimeError("Profiler is not running.")
        self.end_time = self._current_time()
        self.events.append(("stop", self.end_time))

    def get_report(self):
        if self.start_time is None or self.end_time is None:
            raise RuntimeError("Profiler has not been started and stopped properly.")
        duration = self.end_time - self.start_time
        report = {
            "duration": duration,
            "events": self.events
        }
        return report

    def _current_time(self):
        import time
        return time.time()