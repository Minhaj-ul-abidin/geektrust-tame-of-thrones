import unittest ,sys , io
from runner import Runner
from pathlib import Path

input_file1_path = "tests/input1.txt"
output_file1_path = "tests/output1.txt"
input_file2_path = "tests/input2.txt"
output_file2_path = "tests/output2.txt"


class TestRunner(unittest.TestCase):
    def test_run_for_winning(self):
        with Path(output_file1_path).open("r") as f:
            output = f.read().strip()
        
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        Runner(input_file1_path)
        val = new_stdout.getvalue().strip()
        sys.stdout = old_stdout
        self.assertEqual(val,output)
    
    def test_run_for_loosing(self):
        with Path(output_file2_path).open("r") as f:
            output = f.read().strip()
        
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        Runner(input_file2_path)
        val = new_stdout.getvalue().strip()
        sys.stdout = old_stdout
        self.assertEqual(val,output)