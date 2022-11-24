Using `pip-compile` from `pip-tools`:
```
pip-compile --resolver=backtracking --output-file=- > requirements.txt
pip install -r requirements.txt
```