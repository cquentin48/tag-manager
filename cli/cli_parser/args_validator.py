VALIDATOR_ARGS_CHANGELOG_OK = 1
VALIDATOR_ARGS_NAME_OK = 2
VALIDATOR_ARGS_NUMBER_OK = 3
VALIDATOR_ARGS_MESSAGE_OK = 4
VALIDATOR_ARGS_CHANGELOG_NO_NAME = 11
VALIDATOR_ARGS_CHANGELOG_NO_VERSION_NUMBER = 12
VALIDATOR_ARGS_CHANGELOG_NO_MESSAGE = 13
VALIDATOR_ARGS_NAME_NO_NAME = 21
VALIDATOR_ARGS_NUMBER_NO_NUMBER = 31
VALIDATOR_ARGS_MESSAGE_NO_MESSAGE = 41
VALIDATOR_ARGS_UNKOWN_OUTPUT = 51
VALIDATOR_ARGS_NO_COMMIT_MESSAGE = 61


class ArgsValidator:
    """CLI arguments validator
    """

    def __init__( # pylint: disable=too-many-arguments
        self,
        output: str,
        name:str="",
        version:str="",
        changelog:str="",
        commit_message:str=""
    ):
        """Class constructor

        Args:
            name (str): tag name entered
            version (str): tag version number entered
            changelog (str): tag changelog entered
            output (str): where the data should be directed
            commit_message (str): Last commit message
        """
        self.name = name
        self.version = version
        self.changelog = changelog
        self.output = output
        self.commit_message = commit_message

    def verify_args_changelog(self,
                              name_ok: bool,
                              version_number_ok: bool,
                              commit_message: bool,
                              message_ok: bool) -> int:
        """Verify the changelog file update ouput with the input given by the user

        Args:
            name_ok (bool): If the name is correctly given
            version_number_ok (bool): If the version number is correctly given
            message_ok (bool): If the message is correctly given
            commit_message (bool): If the message is a commit message

        Returns:
            int: operation code result
        """
        if not name_ok and not version_number_ok and not message_ok and not commit_message:
            return VALIDATOR_ARGS_NO_COMMIT_MESSAGE
        if not commit_message:
            if not name_ok:
                return VALIDATOR_ARGS_CHANGELOG_NO_NAME
            if not version_number_ok:
                return VALIDATOR_ARGS_CHANGELOG_NO_VERSION_NUMBER
            if not message_ok:
                return VALIDATOR_ARGS_CHANGELOG_NO_MESSAGE
        return VALIDATOR_ARGS_CHANGELOG_OK

    def test_input(self) -> tuple[bool,bool,bool]:
        """Test the args input chosen by the user
        and returns conditions

        Returns:
            tuple[bool,bool,bool]: if the name is ok,
        the version number is ok and if the changelog message is ok
        """
        name_ok = self.name is not None \
            and self.name != ""
        version_number_ok = self.version is not None \
            and self.version != ""
        message_ok = self.changelog is not None \
            and self.changelog != ""
        commit_message_ok = self.commit_message is not None \
            and self.commit_message != ""

        return [name_ok,version_number_ok,message_ok,commit_message_ok]


    def verify_args_display(self,
                            input_given: bool,
                            error_op_code: int,
                            commit_message: bool,
                            success_op_code: int) -> int:
        """Verify the single param display ouput with the input given by the user

        Args:
            input_given (bool): If the name is correctly given
            commit_message (bool): If the commit message is correctly given

        Returns:
            int: operation code result
        """
        if not input_given and not commit_message:
            return error_op_code
        return success_op_code

    def verify_args(self) -> int:
        """Verify the arguments

        Returns:
            int: operation code result
        """
        [name_ok, version_number_ok, message_ok,commit_message_ok] = self.test_input()
        match self.output:
            case "changelog":
                return self.verify_args_changelog(
                    name_ok,
                    version_number_ok,
                    commit_message_ok,
                    message_ok
                )
            case "name":
                return self.verify_args_display(
                    name_ok,
                    VALIDATOR_ARGS_NAME_NO_NAME,
                    commit_message_ok,
                    VALIDATOR_ARGS_NAME_OK
                )
            case "number":
                return self.verify_args_display(
                    version_number_ok,
                    VALIDATOR_ARGS_NUMBER_NO_NUMBER,
                    commit_message_ok,
                    VALIDATOR_ARGS_NUMBER_OK
                )
            case "changelog_message":
                return self.verify_args_display(
                    message_ok,
                    VALIDATOR_ARGS_MESSAGE_NO_MESSAGE,
                    commit_message_ok,
                    VALIDATOR_ARGS_MESSAGE_OK
                )
            case _:
                return VALIDATOR_ARGS_UNKOWN_OUTPUT
