class CLIOutput:
    """Output class which will display
    arg in the shell
    """
    def __init__(self, arg: str) -> None:
        """Class constructor

        Args:
            arg (str): Arg to be displayed
        """
        if arg is None or arg == "":
            raise TypeError("Argument is empty!")
        self.arg = arg

    def output_result(self): #pragma: no cover
        """Display the args result in the output
        """
        print(self.arg)

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o,CLIOutput):
            return False

        arg_eq = __o.arg == self.arg
        return arg_eq
