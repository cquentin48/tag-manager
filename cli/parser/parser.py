import argparse
import sys

from cli.parser.args_validator import ArgsValidator, VALIDATOR_ARGS_CHANGELOG_OK,\
    VALIDATOR_ARGS_MESSAGE_OK, VALIDATOR_ARGS_NAME_OK,VALIDATOR_ARGS_NUMBER_OK


class Parser:
    """CLI parser for tag manager
    """

    def __init__(self):
        """CLI parser constructor
        """
        self.parser = self._init_parser()
        self.output = ""
        self.name = ""
        self.version_number = ""
        self.message = ""
        self.validator = None

    def _init_parser_args(self,parser: argparse.ArgumentParser): #pragma: no cover
        """Add the arguments to the parser

        Args:
            parser (argparse.ArgumentParser): CLI parser
        """
        parser.add_argument('-o','--output',required=True)
        parser.add_argument('-n','--name')
        parser.add_argument('-v','--version')
        parser.add_argument('-c','--changelog')

    def init_args(self, output:str,name:str,version_number:str,message:str):
        """Initialise the args given by the user in the cli

        Args:
            output (str): output type
            name (str): version name
            version_number (str): version number
            message (str): version changes
        """
        self.output = output
        self.name = name
        self.version_number = version_number
        self.message = message

    def verify_args(self, output: str):
        """Verify the args and raises an exception if
        necessary

        Args:
            output (str): output type (changelog|name|number|changelog_message)

        Raises:
            TypeError: Incorrect validation or unknown output type
        """
        validator_args_validation_result = self.validator.verify_args()

        match output:
            case "changelog":
                if validator_args_validation_result != VALIDATOR_ARGS_CHANGELOG_OK:
                    raise TypeError("Incorrect inputs for the changelog file")
            case "name":
                if validator_args_validation_result != VALIDATOR_ARGS_NAME_OK:
                    raise TypeError("Incorrect inputs for the tag name display")
            case "number":
                if validator_args_validation_result != VALIDATOR_ARGS_NUMBER_OK:
                    raise TypeError("Incorrect inputs for the tag version number display")
            case "changelog_message":
                if validator_args_validation_result != VALIDATOR_ARGS_MESSAGE_OK:
                    raise TypeError("Incorrect inputs for the tag message display")
            case _:
                raise TypeError("Incorrect output")


    def update_args(self, args: list):
        """Update the args input by the user
        and set the properties

        Args:
            args (list): Args input of the user
        """
        [output,name,version,message] = self.parse_args(args)
        try:
            self.validator = self.create_validator(output,name,version,message)
            self.verify_args(output)
            self.init_args(output,name,version,message)
        except TypeError as _:
            sys.exit(1)


    def _init_parser(self)->argparse.ArgumentParser: #pragma: no cover
        """Init the parser
        """
        parser = argparse.ArgumentParser(
                prog="Tag manager Parser",
                description="Parser for the tag manager"
                )
        self._init_parser_args(parser)
        return parser

    def parse_args(self, args_input)-> tuple[str,str,str,str]:
        """Parse arguments from the cli and returns it
        as a tuple

        Args:
            args_input (bool): CLI argument inputs given by the user

        Returns:
            tuple[str,str,str,str]: output type, tag name,
                tag version number, tag changelog message
        """
        args = self.parser.parse_args(args=args_input)
        return [args.output,args.name,args.version,args.changelog]

    def create_validator(self,output:str,name:str,number: str,changelog: str)->ArgsValidator:
        """Generates the arguments validator

        Returns:
            ArgsValidator: Validator used in the cli
        """
        return ArgsValidator(output,name,
        number,changelog)
        