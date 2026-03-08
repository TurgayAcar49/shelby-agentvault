import subprocess

def store_output(file):
    subprocess.run(["shelby", "blob", "upload", file])

store_output("agent_output.txt")
