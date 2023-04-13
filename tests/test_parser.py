import unittest

from chat_parser import ChatParser
from utils import get_test_case


class TestClient(unittest.TestCase):
    maxDiff = None
    parser = ChatParser()

    def test_step_1(self):
        self.assert_test_case('step_1')

    def assert_test_case(self, test_step):
        test_case = get_test_case(test_step)
        output = self.parser.parse_chat(test_case['input'])
        self.assertEqual(test_case['output'], output)
