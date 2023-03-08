import unittest

from cli.parser.parser import Parser
from cli.parser.args_validator import ArgsValidator

class TestParser(unittest.TestCase):
    """Parser test case class
    """

    def test_init_validator_ok(self):
        """Check if the given parser
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
        """Test the args parser
        with the args returned and
        the short argument prefix options
        """
        # Given
        output = "changelog"
        name = "New version"
        version_number = "1.0"
        changelog_message = "test message"

        args = [
            "-o", output,
            "-n", name,
            "-v", version_number,
            "-c", changelog_message,
        ]

        parser = Parser()

        # Acts
        [
            operation_output,
            operation_name,
            operation_version_number,
            operation_changelog_message
        ] = parser.parse_args(args)

        # Asserts
        self.assertEqual(operation_output,output)
        self.assertEqual(operation_name,name)
        self.assertEqual(operation_version_number,version_number)
        self.assertEqual(operation_changelog_message,changelog_message)

    def test_parse_args_llong(self):
        """Test the args parser
        with the args returned and
        the long argument prefix options
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
        [
            operation_output,
            operation_name,
            operation_version_number,
            operation_changelog_message
        ] = parser.parse_args(args)

        # Asserts
        self.assertEqual(operation_output,output)
        self.assertEqual(operation_name,name)
        self.assertEqual(operation_version_number,version_number)
        self.assertEqual(operation_changelog_message,changelog_message)
