import os

script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(script_dir, "src")

modules = [
    "AbstractMarker.py",
    "WoundedPreyMarker.py",
    "MarkerSetWrapper.py",
    "attackCalcs.py"
]

# Add any import lines you want to ignore
IGNORED_IMPORTS = [
    "from scripts.src.MarkerSetWrapper import MarkerSetWrapper",
    "from scripts.src.WoundedPreyMarker import LOGIC_MARKER_CLASSES",
    'from scripts.src.AbstractMarker import AbstractMarker',
    'from scripts.constants',
    'from scripts.traitsHandler',
    'from scripts.eventMemory'
]

with open(os.path.join(script_dir, "combined.py"), "w") as outfile:
    for module in modules:
        file_path = os.path.join(src_dir, module)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Module {module} not found in {src_dir}")

        outfile.write(f"# ----- {module} -----\n")
        with open(file_path, "r") as infile:
            for line in infile:
                if any(line.strip().startswith(imp) for imp in IGNORED_IMPORTS):
                    continue  # skip internal imports
                outfile.write(line)
        outfile.write("\n")
