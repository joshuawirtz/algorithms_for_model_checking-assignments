# Development Environment
1. Install python.
2. Create virtual environment inside of directory "I".
    ```
    python -m venv .venv
    ```
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