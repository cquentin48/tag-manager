import unittest

from cli.output.shell_output import CLIOutput

class TestShellOuput(unittest.TestCase):
    """Shell output unit test class
    """
    def test_filled_arg_correct_init(self):
        """A filled constructor shouldn't generate and error
        """
        # Given
        arg = "my argument"

        # Acts
        cli_output = CLIOutput(arg)

        # Asserts
        self.assertEqual(cli_output.arg, arg)

    def test_none_arg_except_init(self):
        """An arg with a None value should generate
        a TypeError exception
        """

        # Given
        arg = None

        # Acts & Asserts
        self.assertRaises(TypeError,CLIOutput, arg)

    def test_empty_arg_except_init(self):
        """An arg with an empty value should generate
        a TypeError exception
        """

        # Given
        arg = ""

        # Acts & Asserts
        self.assertRaises(TypeError,CLIOutput, arg)
