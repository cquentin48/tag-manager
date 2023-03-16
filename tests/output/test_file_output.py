import unittest
import os

from cli.output.file_output import FileOutput

from tests.utils.utils import create_directory, remove_directory

class TestFileOuput(unittest.TestCase):
    """Unit test class for FileOutput class
    from package cli.output
    """

    def test_init_with_no_filepath_output_exception(self):
        """When the users doesn't specify an output file path
        a TypeError exception should be raised
        """
        # Given
        output_file_path = None
        name = "New version"
        version = "1.0"
        message = "Test message"

        # Acts & Assert
        self.assertRaises(TypeError,FileOutput,
        output_file_path,name,version,message)

    def test_init_with_empty_filepath_output_exception(self):
        """When the users specify an empty output file path
        a TypeError exception should be raised
        """
        # Given
        output_file_path = ""
        name = "New version"
        version = "1.0"
        message = "Test message"

        # Acts & Assert
        self.assertRaises(TypeError,FileOutput,
        output_file_path,name,version,message)

    def test_init_with_no_name_output_exception(self):
        """When the users doesn't specify a tag version name 
        a TypeError exception should be raised
        """
        # Given
        output_file_path = "output.txt"
        name = None
        version = "1.0"
        message = "Test message"

        # Acts & Assert
        self.assertRaises(TypeError,FileOutput,
        output_file_path,name,version,message)

    def test_init_with_empty_name_output_exception(self):
        """When the users specify an empty tag version name
        a TypeError exception should be raised
        """
        # Given
        output_file_path = "output.txt"
        name = ""
        version = "1.0"
        message = "Test message"

        # Acts & Assert
        self.assertRaises(TypeError,FileOutput,
        output_file_path,name,version,message)

    def test_init_with_no_tag_version_number_exception(self):
        """When the users doesn't specify an tag version number
        a TypeError exception should be raised
        """
        # Given
        output_file_path = "output.txt"
        name = "New version"
        version = None
        message = "Test message"

        # Acts & Assert
        self.assertRaises(TypeError,FileOutput,
        output_file_path,name,version,message)

    def test_init_with_empty_tag_version_number_output_exception(self):
        """When the users specify an empty tag version number
        a TypeError exception should be raised
        """
        # Given
        output_file_path = "output.txt"
        name = "New version"
        version = ""
        message = "Test message"

        # Acts & Assert
        self.assertRaises(TypeError,FileOutput,
        output_file_path,name,version,message)

    def test_init_with_no_message_output_exception(self):
        """When the users doesn't specify a tag changelog message
        a TypeError exception should be raised
        """
        # Given
        output_file_path = "output.txt"
        name = "New version"
        version = "1.0"
        message = None

        # Acts & Assert
        self.assertRaises(TypeError,FileOutput,
        output_file_path,name,version,message)

    def test_init_with_empty_message_output_exception(self):
        """When the users specify an empty tag changelog message
        a TypeError exception should be raised
        """
        # Given
        output_file_path = "output.txt"
        name = "New version"
        version = "1.0"
        message = ""

        # Acts & Assert
        self.assertRaises(TypeError,FileOutput,
        output_file_path,name,version,message)

    def test_correct_init_should_init_values(self):
        """When the values are correctly specifies, the constructor
        should update the values
        """
        # Given
        output_file_path = "output.txt"
        name = "New version"
        version = "1.0"
        message = "Test message"

        # Acts
        file_output = FileOutput(
            output_file_path,
            name,
            version,
            message
        )

        # Asserts
        self.assertEqual(file_output.file_path,output_file_path)
        self.assertEqual(file_output.name,name)
        self.assertEqual(file_output.version,version)
        self.assertEqual(file_output.message,message)

    def test_get_parent_directory_path_incorrect_file_path_error(self):
        """When the filepath is incorrectly specified, a TypeError
        exception should be raised
        """
        # Given
        output_file_path = "output.txt"
        name = "New version"
        version = "1.0"
        message = "Test message"

        file_output = FileOutput(
            output_file_path,
            name,
            version,
            message
        )

        # Acts & Asserts
        self.assertRaises(TypeError,file_output.get_parent_directory_path)

    def test_get_parent_directory_path_correct_file_path_success(self):
        """When the filepath is correctly specified, the parent directory
        file path should be given
        """
        # Given
        output_file_path = "base_directory/res/output.txt"
        name = "New version"
        version = "1.0"
        message = "Test message"

        file_output = FileOutput(
            output_file_path,
            name,
            version,
            message
        )

        expected_result = "base_directory/res"

        # Acts
        operation_result = file_output.get_parent_directory_path()

        # Asserts
        self.assertEqual(operation_result,expected_result)

    def test_does_parent_directory_path_exist_known_file_path_returns_true(self):
        """When the filepath specified is an actual filepath, the function
        should returns true
        """
        # Given
        output_file_path = os.path.abspath(__file__)
        name = "New version"
        version = "1.0"
        message = "Test message"

        file_output = FileOutput(
            output_file_path,
            name,
            version,
            message
        )

        # Acts
        operation_result = file_output.does_parent_directory_path_exist()

        # Asserts
        self.assertEqual(operation_result,True)

    def test_does_parent_directory_path_exist_unknown_file_path_returns__false(self):
        """When the filepath specified isn't an actual filepath, the function
        should returns false
        """
        # Given
        output_file_path = "/teskmelk/jljl/"
        name = "New version"
        version = "1.0"
        message = "Test message"

        file_output = FileOutput(
            output_file_path,
            name,
            version,
            message
        )

        # Acts
        operation_result = file_output.does_parent_directory_path_exist()

        # Asserts
        self.assertEqual(operation_result,False)

    def test_append_to_file_unkown_parent_directory_path_raises_exception(self):
        """When the filepath specified isn't an actual filepath, the function
        should raise an exception
        """
        # Given
        output_file_path = "/teskmelk/jljl/"
        name = "New version"
        version = "1.0"
        message = "Test message"

        file_output = FileOutput(
            output_file_path,
            name,
            version,
            message
        )

        # Acts & Asserts
        self.assertRaises(FileNotFoundError,file_output.output_result)

    def test_append_to_file_known_parent_directory_path_ok(self):
        """When the parent directory exists (created here), the file is
        created and the data is added
        """
        # Given
        output_file_path = os.path.abspath(__file__)\
            .replace("/tests/output/test_file_output.py","/res/changelog.txt")
        name = "New version"
        version = "1.0"
        message = "Test message"

        directory_path = output_file_path.replace("changelog.txt","")

        file_output = FileOutput(
            output_file_path,
            name,
            version,
            message
        )
        create_directory(directory_path)

        expected_output = [
            "**************",
            "Name: "+name,
            "Version: "+version,
            "---------------",
            "Changelog",
            message,
            "**************",
        ]

        # Acts
        file_output.output_result()

        # Asserts
        with open(output_file_path, 'r',encoding="utf-8") as file:
            lines = file.readlines()
            for i,single_line in enumerate(lines):
                self.assertEqual(
                    single_line.replace('\n',''),
                    expected_output[i]
                )

        # After
        remove_directory(directory_path)

    def test_append_to_file_known_file_path_ok(self):
        """When the file exist, data is appended
        """
        # Given
        output_file_path = os.path.abspath(__file__)\
            .replace("/tests/output/test_file_output.py","/res/changelog.txt")
        name = "New version"
        version = "1.0"
        message = "Test message"

        directory_path = output_file_path.replace("changelog.txt","")

        file_output = FileOutput(
            output_file_path,
            name,
            version,
            message
        )
        create_directory(directory_path)

        expected_output = [
            "**************",
            "Name: "+name,
            "Version: "+version,
            "---------------",
            "Changelog",
            message,
            "**************",
            "**************",
            "Name: "+name,
            "Version: "+version,
            "---------------",
            "Changelog",
            message,
            "**************",
        ]

        # Acts
        file_output.output_result()
        file_output.output_result()

        # Asserts
        with open(output_file_path, 'r',encoding="utf-8") as file:
            lines = file.readlines()
            for i,single_line in enumerate(lines):
                self.assertEqual(
                    single_line.replace('\n',''),
                    expected_output[i]
                )

        # After
        remove_directory(directory_path)

    def test_eq_two_file_output_same_args_equals_true(self):
        """When two file_output objects are created with same arguments
        the equality function should returns true
        """
        # Given
        output_file_path = os.path.abspath(__file__)\
            .replace("/tests/output/test_file_output.py","/res/changelog.txt")
        name = "New version"
        version = "1.0"
        message = "Test message"

        directory_path = output_file_path.replace("changelog.txt","")

        # Acts
        create_directory(directory_path)

        file_output_1 = FileOutput(
            output_file_path,
            name,
            version,
            message
        )

        file_output_2 = FileOutput(
            output_file_path,
            name,
            version,
            message
        )

        # Asserts
        self.assertEqual(file_output_1,file_output_2)

        # After
        remove_directory(directory_path)

    def test_eq_two_file_output_different_args_equals_false(self):
        """When two file_output objects are created with differents arguments
        the equality function should returns false
        """
        # Given
        output_file_path = os.path.abspath(__file__)\
            .replace("/tests/output/test_file_output.py","/res/changelog.txt")
        name = "New version"
        version = "1.0"
        message_1 = "Test message"
        message_2 = "Test message2"

        directory_path = output_file_path.replace("changelog.txt","")

        # Acts
        create_directory(directory_path)

        file_output_1 = FileOutput(
            output_file_path,
            name,
            version,
            message_1
        )

        file_output_2 = FileOutput(
            output_file_path,
            name,
            version,
            message_2
        )

        # Asserts
        self.assertNotEqual(file_output_1,file_output_2)

        # After
        remove_directory(directory_path)

    def test_eq_one_file_output_with_no_file_output_equals_false(self):
        """When one file_output objects is created with one non file-output object
        the equality function should returns false
        """
        # Given
        output_file_path = os.path.abspath(__file__)\
            .replace("/tests/output/test_file_output.py","/res/changelog.txt")
        name = "New version"
        version = "1.0"
        message_1 = "Test message"

        directory_path = output_file_path.replace("changelog.txt","")

        # Acts
        create_directory(directory_path)

        file_output = FileOutput(
            output_file_path,
            name,
            version,
            message_1
        )

        other_object = 1231

        # Asserts
        self.assertNotEqual(file_output,other_object)

        # After
        remove_directory(directory_path)
