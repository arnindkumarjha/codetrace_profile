import unittest
from src.profiler import Profiler

class TestProfiler(unittest.TestCase):

    def setUp(self):
        self.profiler = Profiler()

    def test_start(self):
        self.profiler.start()
        self.assertTrue(self.profiler.is_running)

    def test_stop(self):
        self.profiler.start()
        self.profiler.stop()
        self.assertFalse(self.profiler.is_running)

    def test_get_report(self):
        self.profiler.start()
        self.profiler.stop()
        report = self.profiler.get_report()
        self.assertIsNotNone(report)

if __name__ == '__main__':
    unittest.main()