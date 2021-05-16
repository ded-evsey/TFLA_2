from ..units import Sequence


class DoNothing:
    def __init__(self):
        self.reducible = False

    def __str__(self):
        return 'do-nothing'


class Assign:
    def __init__(self, name='', expression=object()):
        self.name = str(name)
        self.expression = expression
        self.reducible = True

    def __str__(self):
        return f'{self.name} = {self.expression.__str__()}'

    def reduce(self, environment=None):
        if environment is None:
            environment = {}
        r = getattr(self.expression, 'reducible', False)
        if r:
            return {
                'statement': Assign(
                    self.name,
                    self.expression.reduce(environment)
                ),
                'environment': environment
            }
        return {
            'statement': DoNothing(),
            'environment': environment.update({
                self.name: self.expression
            })
        }


class If:
    def __init__(
        self,
        condition=object(),
        consequence=object(),
        alternative=object()
    ):
        self.condition = condition
        self.consequence = consequence
        self.alternative = alternative
        self.reducible = True

    def __str__(self):
        return f'if {self.condition.__str__()}: \n \t {self.consequence} \n else: \n\t {self.alternative}'

    def reduce(self, environment=None):
        if environment is None:
            environment = {}
        r = getattr(self.condition, 'reducible', False)
        if r:
            return {
                'statement': If(
                    self.condition.reduce(environment),
                    self.consequence,
                    self.alternative
                ),
                'environment': environment
            }
        v = getattr(self, 'condition', False)
        if bool(v):
            return {
                'statement': self.consequence,
                'environment': environment
            }
        return {
            'statement': self.alternative,
            'environment': environment
        }


class While:
    def __init__(self, condition=object(), body=object()):
        self.condition = condition
        self.body = body
        self.reducible = True

    def __str__(self):
        return f'while {self.condition}: \n\t {self.body}\n'

    def reduce(self, environment=None):
        if environment is None:
            environment = {}
        return {
            'statement': If(
                self.condition,
                Sequence(
                    self.body,
                    While(
                        self.condition, self.body
                    )
                )
            ),
            'environment': environment
        }

