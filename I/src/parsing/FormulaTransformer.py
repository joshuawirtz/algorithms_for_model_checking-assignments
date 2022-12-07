from lark.visitors import Transformer

class FormulaTransformer(Transformer):
    def start(self, f):
        (f,) = f
        return f
    def formula(self, f):
        (f,) = f
        return f
    
    TRUE = lambda self, _: {"val": True}
    FALSE = lambda self, _: {"val": False}
    def VAR(self, f):
        f = str(f)
        return {"var": f}
    def AL(self, f):
        f = str(f)
        return f
    def land(self, f):
        return {"and": f}
    def lor(self, f):
        return {"or": f}
    def diamond(self, f):
        (a, f) = f
        return {"diamond": [a, f]}
    def box(self, f):
        (a, f) = f
        return {"box": [a, f]}
    def mu(self, f):
        return {"mu": f}
    def nu(self, f):
        return {"nu": f}