# Development Environment
Using `pip-compile` from `pip-tools`:
```
pip-compile --resolver=backtracking --output-file=- > requirements.txt
pip install -r requirements.txt
```
# Lark
## Documentation
https://lark-parser.readthedocs.io/en/latest/visitors.html
## Syntax highlighting
for VSCode/VSCodium:
```
ext install dirk-thomas.vscode-lark
```