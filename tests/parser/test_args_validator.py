import unittest
from cli.parser.args_validator import ArgsValidator,\
    VALIDATOR_ARGS_UNKOWN_OUTPUT, VALIDATOR_ARGS_NUMBER_OK,\
    VALIDATOR_ARGS_CHANGELOG_NO_MESSAGE, VALIDATOR_ARGS_CHANGELOG_NO_NAME,\
    VALIDATOR_ARGS_CHANGELOG_NO_VERSION_NUMBER, VALIDATOR_ARGS_CHANGELOG_OK,\
    VALIDATOR_ARGS_MESSAGE_NO_MESSAGE, VALIDATOR_ARGS_MESSAGE_OK,\
    VALIDATOR_ARGS_NAME_NO_NAME, VALIDATOR_ARGS_NAME_OK, VALIDATOR_ARGS_NUMBER_NO_NUMBER

class TestArgsValidator(unittest.TestCase):
    """Args validator test case class
    """

    def test_verify_args_changelog_ok(self):
        """Check if the validator returns true
        when the parser has every info for the changelog
        """
        # Given
        name = "My version"
        version = "1.0"
        changelog = "Test changelog"
        output = "changelog"

        validator = ArgsValidator(output,name,version,changelog)

        # Acts
        operation_output = validator.verify_args()

        # Asserts
        self.assertEqual(operation_output,VALIDATOR_ARGS_CHANGELOG_OK)

    def test_verify_args_name_ok(self):
        """Check if the validator returns true
        when the parser has every info for the name
        """
        # Given
        name = "My version"
        operation_output = "name"

        validator = ArgsValidator(operation_output,name)

        # Acts
        output = validator.verify_args()

        # Asserts
        self.assertEqual(output,VALIDATOR_ARGS_NAME_OK)

    def test_verify_args_number_ok(self):
        """Check if the validator returns true
        when the parser has every info for the number
        """
        # Given
        number = "1.0"
        operation_output = "number"

        validator = ArgsValidator(operation_output,version=number)

        # Acts
        output = validator.verify_args()

        # Asserts
        self.assertEqual(output,VALIDATOR_ARGS_NUMBER_OK)

    def test_verify_args_changelog_msg_ok(self):
        """Check if the validator returns true
        when the parser has every info for the
        changelog message
        """
        # Given
        changelog = "test_changelog"
        operation_output = "changelog_message"

        validator = ArgsValidator(operation_output,changelog=changelog)

        # Acts
        output = validator.verify_args()

        # Asserts
        self.assertEqual(output,VALIDATOR_ARGS_MESSAGE_OK)

    def test_verify_args_changelog_no_name_error(self):
        """This test should raise an exception when
        the name is not entered with the changelog output
        """
        # Given
        version = "1.0"
        changelog = "Test changelog"
        output = "changelog"

        validator = ArgsValidator(output,version=version,changelog=changelog)

        # Acts
        output = validator.verify_args()

        # Asserts
        self.assertEqual(output,VALIDATOR_ARGS_CHANGELOG_NO_NAME)

    def test_verify_args_changelog_no_number_error(self):
        """This test should raise an exception when
        the version number is not entered with the changelog output
        """
        # Given
        name = "My version"
        changelog = "Test changelog"
        output = "changelog"

        validator = ArgsValidator(output,name=name,changelog=changelog)

        # Acts
        output = validator.verify_args()

        # Asserts
        self.assertEqual(output,VALIDATOR_ARGS_CHANGELOG_NO_VERSION_NUMBER)

    def test_verify_args_changelog_no_changelog_message_error(self):
        """This test should raise an exception when
        the version number is not entered with the changelog output
        """
        # Given
        name = "My version"
        version = "1.0"
        output = "changelog"

        validator = ArgsValidator(output,name=name,version=version)

        # Acts
        output = validator.verify_args()

        # Asserts
        self.assertEqual(output,VALIDATOR_ARGS_CHANGELOG_NO_MESSAGE)

    def test_verify_args_name_no_name_error(self):
        """This test should raise an exception when
        the version name is not entered with the name output
        """
        # Given
        output = "name"

        validator = ArgsValidator(output)

        # Acts
        output = validator.verify_args()

        # Asserts
        self.assertEqual(output,VALIDATOR_ARGS_NAME_NO_NAME)

    def test_verify_args_number_no_number_error(self):
        """This test should raise an exception when
        the version number is not entered with the number output
        """
        # Given
        output = "number"

        validator = ArgsValidator(output)

        # Acts
        output = validator.verify_args()

        # Asserts
        self.assertEqual(output,VALIDATOR_ARGS_NUMBER_NO_NUMBER)

    def test_verify_args_changelog_message_no_message_error(self):
        """This test should raise an exception when
        the version changelog message is not entered with the changelog message output
        """
        # Given
        output = "changelog_message"

        validator = ArgsValidator(output)

        # Acts
        output = validator.verify_args()

        # Asserts
        self.assertEqual(output,VALIDATOR_ARGS_MESSAGE_NO_MESSAGE)

    def test_verify_args_other_output_error(self):
        """This test should raise an exception when
        the version changelog message is not entered with the changelog message output
        """
        # Given
        output = "kmdsqkdmsqkd"

        validator = ArgsValidator(output)

        # Acts
        output = validator.verify_args()

        # Asserts
        self.assertEqual(output,VALIDATOR_ARGS_UNKOWN_OUTPUT)
