import os

script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(script_dir, "src")

modules = [
    "AbstractMarker.py",
    "WoundedPreyMarker.py",
    "MarkerSetWrapper.py",
    "attackCalcs.py"
]

with open(os.path.join(script_dir, "combined.py"), "w") as outfile:
    for module in modules:
        file_path = os.path.join(src_dir, module)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Module {module} not found in {src_dir}")
        with open(file_path, "r") as infile:
            outfile.write(f"# ----- {module} -----\n")
            outfile.write(infile.read() + "\n\n")
