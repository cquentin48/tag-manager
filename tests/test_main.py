import unittest

from cli.main import hello_world

class TestMain(unittest.TestCase):
    """Sample unit test class

    """

    def test_hello_world(self):
        """Check in this test if the
        hello world message is displayed
        """
        # Given

        # Test
        operation_result = \
            hello_world()

        # Asserts
        self.assertEqual(operation_result,"hello world!")
