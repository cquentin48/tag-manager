import argparse

from cli.parser.args_validator import ArgsValidator


class Parser:
    """CLI parser for tag manager
    """

    def __init__(self):
        """CLI parser constructor
        """
        self.parser = self._init_parser()
        self.output = ""
        self.name = ""
        self.number = ""
        self.changelog = ""
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
        