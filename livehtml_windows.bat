@echo off
rem Disables the echoing of commands to standard output to keep the console clean.
cd "C:\insert\here\the\path\to\the\python_script"
rem Changes the working directory of the cmd.exe process to the specified absolute path.
python livehtml.py "C:\insert\here\the\path\to\the\website\index.html"
rem Invokes the Python executable passing the script and the path string as arguments.
