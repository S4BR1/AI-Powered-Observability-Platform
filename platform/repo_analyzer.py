import os
import subprocess
import glob
from ai_stack_detector import detect_stack

def clone_repo(url, path="repo"):
    subprocess.run(["git", "clone", url, path], check=True)

def analyze_repo(path="repo"):
    files = [f for f in glob.glob(path + "/**/*", recursive=True)]
    summary = "\n".join(files)

    stack_info = detect_stack(summary)
    return stack_info
