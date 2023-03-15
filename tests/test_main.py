import unittest
import subprocess
import os
import shutil

from cli.main.main import init_parser
from cli.cli_parser.parser import Parser


class TestMain(unittest.TestCase):
    """Sample unit test class
    """

    def test_init_parser_returns_parser(self):
        """Check in this test if this
        method returns a CLI Parser
        """
        # Given
        args = ['-o', 'name', '-n', 'My version']
        expected_result = Parser()
        expected_result.update_args(args)

        # Test
        operation_result = init_parser(args)

        # Asserts
        self.assertTrue(operation_result == expected_result)

    def test_sample_main_function_display(self):
        """Execute the main function in a terminal
        and check if the result is the expected one
        """
        # Given
        cwd = os.getcwd()
        make_path = cwd.replace("/test/test_main.py","/")
        gen_exec_cmd = ["make", "exec_file_silent"]
        shell_cmd = ["./main", "-o", "name", "-n", "\"My version\""]
        expected_result = "My version\n"

        # Acts
        os.chdir(make_path)
        with subprocess.Popen(gen_exec_cmd) as make_process:
            make_process.wait()
            os.chdir(make_path+"/dist/")
            with subprocess.Popen(shell_cmd,stdout=subprocess.PIPE) as op_process:
                op_process.wait()
                operation_result = op_process.stdout.readlines()[0]
                operation_result = operation_result.decode("utf-8").replace("\"","")

        # Asserts
        self.assertEqual(operation_result, expected_result)

        # After
        os.chdir(make_path)
        shutil.rmtree(make_path+"/dist")
        os.chdir(cwd)

    def test_sample_main_function_changelog_write(self):
        """Execute the main function in a terminal
        and check if the result is the expected one
        """
        # Given
        cwd = os.getcwd()
        make_path = cwd.replace("/test/test_main.py","/")
        gen_exec_cmd = ["make", "exec_file_silent"]
        shell_cmd = [
            "./main",
            "-o", "changelog",
            "-n", "\"My version\"",
            "-v", "\"1.0\"",
            "-c", "My message"
        ]
        expected_result = 0

        # Acts
        os.chdir(make_path)
        with subprocess.Popen(gen_exec_cmd) as make_process:
            make_process.wait()
            os.chdir(make_path+"/dist/")
            with subprocess.Popen(shell_cmd,stdout=subprocess.PIPE) as op_process:
                op_process.wait()
                result = op_process.returncode

        # Asserts
        self.assertEqual(result,expected_result)

        # After
        os.chdir(make_path)
        os.remove(make_path+"/changelog.txt")
        os.chdir(cwd)
