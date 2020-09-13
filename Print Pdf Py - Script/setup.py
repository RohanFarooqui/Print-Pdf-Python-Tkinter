import cx_Freeze

exe = [cx_Freeze.Executable("Print Pdf Python.pyw", base = "Win32GUI")] # <-- HERE

cx_Freeze.setup(
    name = "Print PDF-Python" ,
    version = "1.0",
    options = {"build_exe": {"packages": ["tkinter", "win32api", "win32print", "os"]}},  
    executables = [cx_Freeze.Executable("Print Pdf Python.pyw", base = "Win32GUI",icon="Images\exe.ico")]
) 
