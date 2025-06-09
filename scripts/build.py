modules = [
    "AbstractMarker.py",
    "WoundedPreyMarker.py",
    "MarkerSetWrapper.py",
    "attackCalcs.py"
]

with open("combined.py", "w") as outfile:
    for module in modules:
        with open(f"src/{module}", "r") as infile:
            outfile.write("# ----- " + module + " -----\n")
            outfile.write(infile.read() + "\n\n")
