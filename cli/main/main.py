
import sys

from cli.cli_parser.parser import Parser


def init_parser(args:list)->Parser:
    """Init the CLI cli_parser

    Args:
        args (list): args ented by the user

    Returns:
        Parser: cli cli_parser generated
    """
    cli_parser = Parser()
    cli_parser.update_args(args)
    return cli_parser


if __name__ == '__main__': # pragma: no cover
    parser = init_parser(sys.argv[1:])
    parser.output_result()
