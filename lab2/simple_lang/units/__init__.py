
class Sequence:
    def __init__(self, first=object(), second=object()):
        self.first = first
        self.second = second
        self.reducible = True

    def __str__(self):
        return f'{self.first.__str__()} {self.second.__str__()}'

    def reduce(self, environment):
        if self.first.__str__() == 'do-nothing':
            return {
                'statement': self.second,
                'environment': environment
            }
        statement, environment = self.reduce(environment).values()
        return {
            'statement': Sequence(statement, self.second),
            'environment': environment
        }


class Variable:
    def __init__(self, name=''):
        self.name = str(name)
        self.reducible = True

    def __str__(self):
        return self.name

    def reduce(self, environment=None):
        if environment is None:
            environment = {}
        return environment.get(self.name, 'Not value variable')
