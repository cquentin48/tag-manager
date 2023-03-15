import argparse
import os
import sys


from .args_validator import ArgsValidator, VALIDATOR_ARGS_CHANGELOG_OK,\
    VALIDATOR_ARGS_MESSAGE_OK, VALIDATOR_ARGS_NAME_OK,VALIDATOR_ARGS_NUMBER_OK
from ..output.file_output import FileOutput
from ..output.shell_output import CLIOutput


class Parser: # pylint: disable=too-many-instance-attributes
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
        self.commit_message = ""
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
        parser.add_argument('-cm','--commitmessage')

    def output_result(self):
        """Output the result of the cli_parser
        """
        self.output_obj.output_result()

    def init_args(self, # pylint: disable=too-many-arguments
        output:str,
        name:str,
        version_number:str,
        message:str
    ):
        """Initialise the args given by the user in the cli

        Args:
            output (str): output type
            name (str): version name
            version_number (str): version number
            message (str): version changes
            commit_message (str): last commit message
        """
        self.output = output
        self.name = name
        self.version_number = version_number
        self.message = message

    def parse_commit_message(self,commit_message: str):
        """Parse the commit message and init the data

        Args:
            commit_message (str): Last commit message entered
            by user
        """
        commit_message_lines = commit_message.split("\n")
        self.name = commit_message_lines[0].replace("[Release]","")
        self.version_number = commit_message_lines[1].replace("Version:","")
        self.message = "\n".join(commit_message_lines[3:])

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o,Parser):
            return False

        output_str_eq = self.output == __o.output
        message_eq = self.name == __o.message
        version_number_eq = self.version_number == __o.message
        message_eq = self.message == __o.message
        output_obj_eq = self.output_obj == __o.output_obj
        commit_message_eq = self.commit_message == __o.commit_message

        return output_str_eq and message_eq\
            and version_number_eq and output_obj_eq and commit_message_eq

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
        [output,name,version,message,commit_message] = self.parse_args(args)
        try:
            self.validator = self.create_validator(output,name,version,message,commit_message)
            self.verify_args(output)
            if commit_message != None and commit_message != "":
                self.output = output
                self.parse_commit_message(commit_message)
            else:
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

    def parse_args(self, args_input)-> tuple[str,str,str,str,str]:
        """Parse arguments from the cli and returns it
        as a tuple

        Args:
            args_input (bool): CLI argument inputs given by the user

        Returns:
            tuple[str,str,str,str,str]: output type, tag name,
                tag version number, tag changelog message and
                commit message
        """
        args = self.parser.parse_args(args=args_input)
        return [args.output,args.name,args.version,args.changelog,args.commitmessage]

    def create_validator(self, # pylint: disable=too-many-arguments
        output:str,name:str,number: str,changelog: str,
        commit_message: str="")->ArgsValidator:
        """Generates the arguments validator

        Returns:
            ArgsValidator: Validator used in the cli
        """
        return ArgsValidator(output,name,
        number,changelog,commit_message)
        