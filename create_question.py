from rich.console import Console, Group
import sys
import os
import pyfiglet
from rich import print
from rich.panel import Panel
from rich import box
console = Console()
import subprocess
def create_question(name):
    
    DSA_TEXT =f"[bold yellow]{pyfiglet.figlet_format("STUPID DSA")}[/bold yellow]"
    INFO_TEXT = Panel.fit(f"[bold green]📁 Setting up problem: [white]{name}[/white][/bold green]",style="bold green")
    
    base_dir = os.path.join(os.getcwd(), name)
    os.makedirs(base_dir, exist_ok=True)
    
    config_dir=os.path.join(base_dir,".vscode")
    os.makedirs(config_dir,exist_ok =True)
    
    cpp_path = os.path.join(base_dir, f"{name}.cpp")
    in_path = os.path.join(base_dir, "input.txt")
    out_path = os.path.join(base_dir, "output.txt")
    vscode_file=os.path.join(config_dir, "tasks.json")
    vscode_cpp_config=os.path.join(config_dir,"c_cpp_properties.json")
    with open(cpp_path, "w") as f:
        f.write(f"""#include <bits/stdc++.h>
using namespace std;

int main() {{

    return 0;
}}
""")
    with open(vscode_file,"w") as f:
        f.write('''
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "compile and run current cpp",
      "type": "shell",
      "command": "cmd.exe",
      "args": [
        "/c",
        "g++ -std=c++17 -o ${fileBasenameNoExtension}.exe ${file} && ${fileBasenameNoExtension}.exe < input.txt > output.txt"
      ],
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "problemMatcher": [],
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      }
    }
  ]
}


''')
    with open(vscode_cpp_config,"w") as f:
        f.write('''
    {
  "configurations": [
    {
      "name": "Win32",
      "includePath": [
        "${workspaceFolder}/**",
        "C:/msys64/mingw64/include/c++/13.2.0",
        "C:/msys64/mingw64/include/c++/13.2.0/x86_64-w64-mingw32",
        "C:/msys64/mingw64/include",
        "C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/13.2.0/include"
      ],
      "compilerPath": "C:/msys64/mingw64/bin/g++.exe",
      "intelliSenseMode": "windows-gcc-x64",
      "cppStandard": "c++17"
    }
  ],
  "version": 4
}

''')
    open(in_path, "w").close()
    open(out_path, "w").close()

    CREATE_TEXT = Panel.fit(f"[bold cyan]✅ Created {cpp_path}, input.txt, and output.txt[/bold cyan]",style="bold cyan")
    END_TEXT=Panel.fit("🎉 Happy Coding! 🚀", style="bold magenta")
    # Combine everything into a Group
    ALL_TEXT = Group(DSA_TEXT, INFO_TEXT, CREATE_TEXT,END_TEXT)
    console.print(Panel.fit(Panel.fit(ALL_TEXT),style="bold yellow"))
    subprocess.run(f"code {base_dir}", shell=True)

    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[red]Usage: python create_question.py <question_name>[/red]")
    else:
        create_question(sys.argv[1])
