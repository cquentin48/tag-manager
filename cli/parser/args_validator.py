
class ArgsValidator:
    """CLI arguments validator
    """

    def __init__(self, output: str, name:str="", version:str="",changelog:str=""):
        """Class constructor

        Args:
            name (str): tag name entered
            version (str): tag version number entered
            changelog (str): tag changelog entered
            output (str): where the data should be directed
        """
        self._name = name
        self._version = version
        self._changelog = changelog
        self._output = output

    def verify_args(self) -> bool:
        """Verify the arguments

        Raises:
            TypeError: Data not found

        Returns:
            bool: True -> yes
        """
        name_ok = self._name is not None \
            and self._name != ""
        version_ok = self._version is not None \
            and self._version != ""
        changelog_ok = self._changelog is not None \
            and self._changelog != ""
        match self._output:
            case "changelog":
                if not name_ok:
                    raise TypeError("No version name entered")
                if not version_ok:
                    raise TypeError("No version number entered")
                if not changelog_ok:
                    raise TypeError("No version number entered")
                return True
            case "name":
                if not name_ok:
                    raise TypeError("No version name entered")
                return True
            case "number":
                if not version_ok:
                    raise TypeError("No version number entered")
                return True
            case "changelog_message":
                if not changelog_ok:
                    raise TypeError("No version changelog entered")
                return True
            case _:
                raise TypeError("Unkown output!")
