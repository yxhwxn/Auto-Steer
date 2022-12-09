"""Test AutoSteer-G's PrestoDB connector"""
from connectors.presto_connector import PrestoConnector
import unittest


class TestPrestoConnector(unittest.TestCase):
    """TestCase for PrestoDB connector"""

    def setUp(self) -> None:
        self.connector = PrestoConnector()
        self.connector.connect()

    def tearDown(self) -> None:
        self.connector.close()

    def test_explain(self):
        result = self.connector.explain('SELECT 42')
        self.assertTrue(result.startswith('{'))

    def test_execution(self):
        result = self.connector.execute('SELECT 42')
        self.assertEqual(result.result[0][0], 42)
        self.assertGreater(result.time_usecs, 0)

    def test_disable_knobs(self):
        knobs = PrestoConnector.get_knobs()
        self.connector.set_disabled_knobs([])
        # test that all knobs are turned on
        self.assertTrue(all(self.connector.get_knob(knob) for knob in knobs))
        self.connector.set_disabled_knobs(knobs)
        # test that all knobs are turned off
        self.assertTrue(not any(self.connector.get_knob(knob) for knob in knobs))
        # turn on all knobs
        self.connector.set_disabled_knobs([])
        self.assertTrue(all(self.connector.get_knob(knob) for knob in knobs))

    def test_num_knobs(self):
        self.assertEqual(len(PrestoConnector.get_knobs()), 7)


if __name__ == '__main__':
    unittest.main()