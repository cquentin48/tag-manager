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

    def display_result(self): #pragma: no cover
        """Display the args result in the output
        """
        print(self.arg)
