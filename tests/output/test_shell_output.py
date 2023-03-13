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

    def test_eq_two_identical_shell_objects_true(self):
        """Two shell objects with identical properties
        should return True
        """

        # Given
        arg = "My arg"

        # Acts
        first_cli_output = CLIOutput(arg)
        second_cli_output = CLIOutput(arg)

        # Assert
        self.assertTrue(first_cli_output == second_cli_output)

    def test_eq_two_differents_shell_objects_false(self):
        """Two shell objects with differents properties
        should return False
        """

        # Given
        first_arg = "My arg"
        second_arg = "My arg2"

        # Acts
        first_cli_output = CLIOutput(first_arg)
        second_cli_output = CLIOutput(second_arg)

        # Assert
        self.assertFalse(
            first_cli_output == second_cli_output
        )

    def test_eq_one_shell_object_with_other_non_shell_object_false(self):
        """One Shell output object and another non Shell
        output object should return Flase
        """

        # Given
        arg = "My arg"

        # Acts
        cli_output = CLIOutput(arg)
        number = 3

        # Assert
        self.assertFalse(cli_output == number)
