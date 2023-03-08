import os

class FileOutput:
    """Class which will write to
    the changelog file
    """
    def __init__(self, output_filepath: str, name: str, version: str, message: str):
        """Class constructor

        Args:
            filoutput_filepathe_output (str): output file path
            name (str): Tag name
            version (str): Tag version
            message (str): Tag changes message
        """
        if output_filepath is None or output_filepath == "" :
            raise TypeError("The filepath hasn't been filled!")
        if name is None or name == "" :
            raise TypeError("The version name hasn't been filled!")
        if version is None or version == "" :
            raise TypeError("The version number hasn't been filled!")
        if message is None or message == "" :
            raise TypeError("The changelog message hasn't been filled!")

        self.file_path:str = output_filepath
        self.name:str = name
        self.version:str = version
        self.message:str = message

    def get_parent_directory_path(self)-> str:
        """Get the parent directory path of the output file_path

        Returns:
            str: parent directory file path
        """
        path_list:list = self.file_path.split("/")
        parent_file_path_list:list = path_list[:-1]
        parent_file_path_file = parent_file_path_list.join("/")
        return parent_file_path_file

    def does_parent_directory_path_exist(self)-> bool:
        """Check if the output file parent directory path
        exists and is a directory

        Returns:
            bool: True yes | False no
        """
        parent_directory_path = self.get_parent_directory_path()
        return os.path.isdir(parent_directory_path)

    def append_to_file(self):
        """Appends the results in the changefile.
        If the folder doesn't exists, an exception is
        raised.

        Otherwise, if the file doesn't exists, it's created.

        Otherwise, it just append the content to the later.
        """
        output_mode = "a+"
        if not self.does_parent_directory_path_exist():
            raise FileNotFoundError("parent-directory-path-not-found")
        if self.does_parent_directory_path_exist() and not os.path.exists(self.file_path):
            output_mode = 'w+'
        else:
            output_mode = 'a+'

        with open(self.file_path,output_mode,mode=output_mode,encoding="utf-8") as file:
            file.write("**************")
            file.write("Name : "+str(self.name))
            file.write("Version: "+str(self.version))
            file.write("---------------")
            file.write("Changelog")
            file.write(str(self.message))
            file.write("**************")
