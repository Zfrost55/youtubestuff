import cx_Freeze
import os.path

executables = [cx_Freeze.Executable("pythonpractice.py")]
os.environ['TCL_LIBRARY'] = r'C:\Users\zdavi\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\zdavi\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'
cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files":["racecar.png"]}},
    executables = executables
    )
