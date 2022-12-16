μCh is a model checker for labelled transition systems. It can read labelled transition systems in the
Aldebaran file format and μ-calculus formulae as defined in the assignment. Checking a formula on a
system can be done using either the naive or Emerson Lei algorithm.

# Development Environment
1. Install python.
2. Create virtual environment inside of directory "I".
    ```
    python -m venv .venv
    ```
   <mark>For the virtual environment to be detected correctly by VSCode/VSCodium make sure to open folder "I" instead of the top-level directory of the repository.</mark>
3. Activate virtual environment.
    - Linux:
        ```
        source .venv/bin/activate
        ```
    - Windows:
        ```
        source .venv/Scripts/activate
        ```
4. Install `pip-tools` for dependency management:
    ```
    pip install pip-tools
    ```
5. Create list of install requirements using `pip-compile` and install them:
    ```
    pip-compile --resolver=backtracking --output-file=- > requirements.txt
    pip install -r requirements.txt
    ```

# Distribution
Distribution images are built using `pyinstaller`:
```
pyinstaller --add-data "src/parsing/grammars:parsing/grammars" src/muCh.py 
```

# Lark
## Documentation
Visit [Lark’s documentation](https://lark-parser.readthedocs.io/en/latest/visitors.html)

## Parser IDE
For testing new grammars use
[Lark IDE](https://www.lark-parser.org/ide/).

## Syntax highlighting
for VSCode/VSCodium:
```
ext install dirk-thomas.vscode-lark
```