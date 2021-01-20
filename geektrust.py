import sys
from pathlib import Path
from runner import Runner
if __name__ == "__main__":
    file_path = sys.argv[1]
    Runner(file_path,candidate_ruler="SPACE")