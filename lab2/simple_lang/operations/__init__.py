from ..types import Number, Boolean


class Operation:
    def __init__(self, left=object(), right=object()):
        self.left = left
        self.right = right
        self.reducible = True

    def __str__(self, operator=''):
        return f'{self.left.__str__()} { operator } {self.right.__str__()}'

    def reduce(self):
        return (
            getattr(self.left, 'reducible', False),
            getattr(self.right, 'reducible', False),
            getattr(self.left, 'value', 0),
            getattr(self.right, 'value', 0)
        )


class Add(Operation):
    def __str__(self, operator='+'):
        return super().__str__(operator)

    def reduce(self, environment=None):
        if environment is None:
            environment = {}
        r_left, r_right, v_left, v_right = super().reduce()
        if r_left:
            return Add(self.left.reduce(environment), self.right)
        if r_right:
            return Add(self.left, self.right.reduce(environment))
        return Number(int(self.left) + int(self.right))


class Multiply(Operation):
    def __str__(self, operator='*'):
        return super().__str__(operator)

    def reduce(self, environment=None):
        if environment is None:
            environment = {}
        r_left, r_right, v_left, v_right = super().reduce()
        if r_left:
            return Multiply(self.left.reduce(environment), self.right)
        if r_right:
            return Multiply(self.left, self.right.reduce(environment))
        return Number(int(self.left) and int(self.right))


class Division(Operation):
    def __str__(self, operator='/'):
        return super().__str__(operator)

    def reduce(self, environment=None):
        if environment is None:
            environment = {}
        r_left, r_right, v_left, v_right = super().reduce()
        if r_left:
            return Division(self.left.reduce(environment), self.right)
        if r_right:
            return Division(self.left, self.right.reduce(environment))
        return Number(int(self.left) / int(self.right))


class Subtraction(Operation):
    def __str__(self, operator='-'):
        return super().__str__(operator)

    def reduce(self, environment=None):
        if environment is None:
            environment = {}
        r_left, r_right, v_left, v_right = super().reduce()
        if r_left:
            return Subtraction(self.left.reduce(environment), self.right)
        if r_right:
            return Subtraction(self.left, self.right.reduce(environment))
        return Number(int(self.left) - int(self.right))


class Less(Operation):
    def __str__(self, operator='<'):
        return super().__str__(operator)

    def reduce(self, environment=None):
        if environment is None:
            environment = {}
        r_left, r_right, v_left, v_right = super().reduce()
        if r_left:
            return Less(self.left.reduce(environment), self.right)
        if r_right:
            return Less(self.left, self.right.reduce(environment))
        return Boolean(int(self.left) < int(self.right))


class More(Operation):
    def __str__(self, operator='>'):
        return super().__str__(operator)

    def reduce(self, environment=None):
        if environment is None:
            environment = {}
        r_left, r_right, v_left, v_right = super().reduce()
        if r_left:
            return More(self.left.reduce(environment), self.right)
        if r_right:
            return More(self.left, self.right.reduce(environment))
        return Boolean(int(self.left) > int(self.right))


class And(Operation):
    def __str__(self, operator='&'):
        return super().__str__(operator)

    def reduce(self, environment=None):
        if environment is None:
            environment = {}
        r_left, r_right, v_left, v_right = super().reduce()
        if r_left:
            return And(self.left.reduce(environment), self.right)
        if r_right:
            return And(self.left, self.right.reduce(environment))
        return Boolean(bool(self.left) and bool(self.right))


class Or(Operation):
    def __str__(self, operator='|'):
        return super().__str__(operator)

    def reduce(self, environment=None):
        if environment is None:
            environment = {}
        r_left, r_right, v_left, v_right = super().reduce()
        if r_left:
            return Or(self.left.reduce(environment), self.right)
        if r_right:
            return Or(self.left, self.right.reduce(environment))
        return Boolean(bool(self.left) or bool(self.right))


class Not:
    def __init__(self, value):
        self.value = value
        self.reducible = True

    def __str__(self):
        return f'! {self.value.__str__()}'

    def reduce(self, environment=None):
        if environment is None:
            environment = {}
        r = getattr(self.value, 'reducible', False)
        v = getattr(self.value, 'value', True)
        if r:
            return Not(self.value.reduce(environment))
        return Boolean(not bool(v))
