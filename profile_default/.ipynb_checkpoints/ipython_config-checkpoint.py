from os import getcwd
c.InteractiveShellApp.exec_lines = [
    'import sys; sys.path.append(getcwd() +'/python-traffictoolbox/')'
]
