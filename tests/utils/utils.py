from pathlib import Path
import shutil

def create_directory(path:str):
    """Creates a directory at the path given

    Args:
        path (str): New directory path
    """
    Path(path).mkdir(parents=True,exist_ok=True)


def remove_directory(path: str):
    """Deletes a directory

    Args:
        path (str): Directory path
    """
    shutil.rmtree(path)
