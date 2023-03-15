import unittest
from unittest.mock import patch

from cli.output.shell_output import CLIOutput

from cli.cli_parser.parser import Parser
from cli.cli_parser.args_validator import ArgsValidator

class TestParser(unittest.TestCase):
    """Parser test case class
    """

    def test_init_validator_ok(self):
        """Check if the given cli_parser
        is correctly configured
        """
        # Given
        output = "changelog"
        name = "New version"
        number = "1.0"
        changelog_message = "test message"

        args_validator = ArgsValidator(output,name,number,changelog_message)

        parser = Parser()

        # Acts
        operation_output = parser.create_validator(output,name,number,changelog_message)

        # Asserts
        self.assertEqual(operation_output.changelog,args_validator.changelog)
        self.assertEqual(operation_output.name,args_validator.name)
        self.assertEqual(operation_output.output,args_validator.output)
        self.assertEqual(operation_output.version,args_validator.version)

    def test_parse_args_short(self):
        """Test the args cli_parser
        with the args returned and
        the short argument prefix options
        """
        # Given
        output = "changelog"
        name = "New version"
        version_number = "1.0"
        changelog_message = "test message"
        commit_message = "My message"

        args = [
            "-o", output,
            "-n", name,
            "-v", version_number,
            "-c", changelog_message,
            "-cm", commit_message,
        ]

        parser = Parser()

        # Acts
        [
            operation_output,
            operation_name,
            operation_version_number,
            operation_changelog_message,
            operation_changelog_commit_message,
        ] = parser.parse_args(args)

        # Asserts
        self.assertEqual(operation_output,output)
        self.assertEqual(operation_name,name)
        self.assertEqual(operation_version_number,version_number)
        self.assertEqual(operation_changelog_message,changelog_message)
        self.assertEqual(operation_changelog_commit_message,commit_message)

    def test_parse_args_llong(self):
        """Test the args cli_parser
        with the args returned and
        the long argument prefix options
        """
        # Given
        output = "changelog"
        name = "New version"
        version_number = "1.0"
        changelog_message = "test message"
        commit_message = "My commit message"

        args = [
            "--output", output,
            "--name", name,
            "--version", version_number,
            "--changelog", changelog_message,
            "--commitmessage", commit_message
        ]

        parser = Parser()

        # Acts
        [
            operation_output,
            operation_name,
            operation_version_number,
            operation_changelog_message,
            operation_changelog_commit_message
        ] = parser.parse_args(args)

        # Asserts
        self.assertEqual(operation_output,output)
        self.assertEqual(operation_name,name)
        self.assertEqual(operation_version_number,version_number)
        self.assertEqual(operation_changelog_message,changelog_message)
        self.assertEqual(operation_changelog_commit_message,commit_message)

    def test_update_args_no_commit_message_ok(self):
        """This function should correctly parse args
        and update the cli_parser with no commit messages
        entered
        """
        # Given
        output = "changelog"
        name = "New version"
        version_number = "1.0"
        changelog_message = "test message"

        args = [
            "--output", output,
            "--name", name,
            "--version", version_number,
            "--changelog", changelog_message,
        ]

        parser = Parser()

        # Acts
        parser.update_args(args)

        # Asserts
        self.assertEqual(parser.output,output)
        self.assertEqual(parser.name,name)
        self.assertEqual(parser.version_number,version_number)
        self.assertEqual(parser.message,changelog_message)

    def test_update_args_commit_message_ok(self):
        """This function should correctly parse args
        and update the cli_parser with no messages
        entered
        """
        # Given
        output = "changelog"
        parser = Parser()
        commit_message = "[Release]RELEASE_NAME\n"+\
            "Version:VERSION_NUMBER\n"+\
            "Changes:\n"+\
            "CHANGELOG"
        expected_name = "RELEASE_NAME"
        expected_version_number = "VERSION_NUMBER"
        expected_changelog_message = "CHANGELOG"

        args = [
            "--output", output,
            "--commitmessage", commit_message,
        ]

        parser = Parser()

        # Acts
        parser.update_args(args)

        # Asserts
        self.assertEqual(parser.output,output)
        self.assertEqual(parser.name,expected_name)
        self.assertEqual(parser.version_number,expected_version_number)
        self.assertEqual(parser.message,expected_changelog_message)

    def test_update_args_fails_raise_except(self):
        """This function with incorrect input should raise
        an exception and exit 
        """
        # Given
        output = "mlkmk"
        name = "New version"
        version_number = "1.0"
        changelog_message = "test message"

        args = [
            "--output", output,
            "--name", name,
            "--version", version_number,
            "--changelog", changelog_message,
        ]

        parser = Parser()

        # Acts & Assert
        self.assertRaises(SystemExit,parser.update_args,args)

    def test_verify_args_incorrect_name_type_error(self):
        """The method verify_args of the tested should raise
        a TypeError if the version name entered is incorrect
        """
        # Given
        # Given
        output = "name"
        name = ""
        version_number = "1.0"
        changelog_message = "test message"

        args = [
            "--output", output,
            "--name", name,
            "--version", version_number,
            "--changelog", changelog_message,
        ]

        parser = Parser()

        # Acts & Assert
        self.assertRaises(SystemExit,parser.update_args,args)

    def test_verify_args_incorrect_version_number_type_error(self):
        """The method verify_args of the tested should raise
        a TypeError if the version number entered is incorrect
        """
        # Given
        # Given
        output = "number"
        name = "My version"
        version_number = ""
        changelog_message = "test message"

        args = [
            "--output", output,
            "--name", name,
            "--version", version_number,
            "--changelog", changelog_message,
        ]

        parser = Parser()

        # Acts & Assert
        self.assertRaises(SystemExit,parser.update_args,args)

    def test_verify_args_incorrect_changelog_type_error(self):
        """The method verify_args of the tested should raise
        a TypeError if the version changelog entered is incorrect
        """
        # Given
        # Given
        output = "changelog_message"
        name = "My version"
        version_number = "1.0"
        changelog_message = ""

        args = [
            "--output", output,
            "--name", name,
            "--version", version_number,
            "--changelog", changelog_message,
        ]

        parser = Parser()

        # Acts & Assert
        self.assertRaises(SystemExit,parser.update_args,args)

    def test_eq_two_identical_objects_should_returns_true(self):
        """Check if the equality method returns True when two
        objects are created with identical properties
        """
        # Given
        args = ['-o', 'name','-n','My version']

        first_parser = Parser()
        second_parser = Parser()

        # Acts
        first_parser.update_args(args)
        second_parser.update_args(args)

        # Asserts
        self.assertTrue(first_parser == second_parser)

    def test_eq_two_differents_parser_should_returns_false(self):
        """Check if the equality method returns False when two
        cli_parser are created with differents properties
        """
        # Given
        first_args = ['-o', 'name','-n','My version']
        second_args = ['-o', 'name','-n','Old version']

        first_parser = Parser()
        second_parser = Parser()

        # Acts
        first_parser.update_args(first_args)
        second_parser.update_args(second_args)

        # Asserts
        self.assertTrue(first_parser != second_parser)

    def test_eq_two_differents_objects_should_returns_false(self):
        """Check if the equality method returns False when an cli_parser
        and another object are created
        """
        # Given
        first_args = ['-o', 'name','-n','My version']
        number = 3

        first_parser = Parser()

        # Acts
        first_parser.update_args(first_args)

        # Asserts
        self.assertTrue(first_parser != number)

    def test_init_output_number_cli_output(self):
        """The method init_output should create a CLI Output
        when the output number is selected
        """
        # Given
        parser = Parser()
        output = "number"
        version_number = "1.0"

        # Acts
        parser.version_number = version_number
        parser.init_output(output)

        # Asserts
        self.assertTrue(isinstance(parser.output_obj,CLIOutput))

    def test_init_output_changelog_message_cli_output(self):
        """The method init_output should create a CLI Output
        when the output changelog_message is selected
        """
        # Given
        parser = Parser()
        output = "changelog_message"
        changelog_message = "My message"

        # Acts
        parser.message = changelog_message
        parser.init_output(output)

        # Asserts
        self.assertTrue(isinstance(parser.output_obj,CLIOutput))

    @patch('builtins.print')
    def test_output_result(self, print_):
        """This function should output the
        content asked by the user either in the changelog
        file or the shell terminal
        """
        # Given
        parser = Parser()
        output = "changelog_message"
        changelog_message = "My message"
        args = ['-o',output,'-c',changelog_message]
        parser.update_args(args)

        # Acts
        parser.output_result()

        # Asserts
        print_.assert_called_with(changelog_message)

    def test_parse_commit_message(self):
        # Given
        parser = Parser()
        commit_message = "[Release]RELEASE_NAME\n"+\
            "Version:VERSION_NUMBER\n"+\
            "Changes:\n"+\
            "CHANGELOG"
        expected_name = "RELEASE_NAME"
        expected_version_number = "VERSION_NUMBER"
        expected_changelog_message = "CHANGELOG"

        # Acts
        parser.parse_commit_message(commit_message)

        # Assert
        self.assertEqual(parser.name,expected_name)
        self.assertEqual(parser.version_number,expected_version_number)
        self.assertEqual(parser.message,expected_changelog_message)

