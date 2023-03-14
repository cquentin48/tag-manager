import argparse
import os
import sys


from .args_validator import ArgsValidator, VALIDATOR_ARGS_CHANGELOG_OK,\
    VALIDATOR_ARGS_MESSAGE_OK, VALIDATOR_ARGS_NAME_OK,VALIDATOR_ARGS_NUMBER_OK
from ..output.file_output import FileOutput
from ..output.shell_output import CLIOutput


class Parser:
    """CLI cli_parser for tag manager
    """

    def __init__(self):
        """CLI cli_parser constructor
        """
        self.parser = self._init_parser()
        self.output = ""
        self.output_obj = None
        self.name = ""
        self.version_number = ""
        self.message = ""
        self.validator = None

    def _init_parser_args(self,parser: argparse.ArgumentParser): #pragma: no cover
        """Add the arguments to the cli_parser

        Args:
            parser (argparse.ArgumentParser): CLI cli_parser
        """
        parser.add_argument('-o','--output',required=True)
        parser.add_argument('-n','--name')
        parser.add_argument('-v','--version')
        parser.add_argument('-c','--changelog')

    def output_result(self):
        """Output the result of the cli_parser
        """
        self.output_obj.output_result()

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

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o,Parser):
            return False

        output_str_eq = self.output == __o.output
        message_eq = self.name == __o.message
        version_number_eq = self.version_number == __o.message
        message_eq = self.message == __o.message
        output_obj_eq = self.output_obj == __o.output_obj

        return output_str_eq and message_eq\
            and version_number_eq and output_obj_eq

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
            self.init_output(self.output)
        except TypeError as _:
            sys.exit(1)

    def init_output(self, output: str):
        """Init the output type

        Args:
            output (str): Type of output chosen by user
        """
        match output:
            case "changelog":
                changelog_parent_directory_path =\
                    os.path.dirname(sys.executable).replace("/dist","/")
                self.output_obj = \
                    FileOutput(
                        changelog_parent_directory_path+"/changelog.txt",
                        self.name,
                        self.version_number,
                        self.message
                    )
            case "name":
                self.output_obj = CLIOutput(self.name)
            case "number":
                self.output_obj = CLIOutput(self.version_number)
            case "changelog_message":
                self.output_obj = CLIOutput(self.message)



    def _init_parser(self)->argparse.ArgumentParser: #pragma: no cover
        """Init the cli_parser
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
        