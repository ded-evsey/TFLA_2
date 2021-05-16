class Value:
    def __init__(self, value):
        self.value = value
        self.reducible = False

    def __str__(self):
        return self.value


class Boolean(Value):
    def __init__(self, value=False):
        value = super().__init__(value)
        self.value = bool(value)

    def __bool__(self):
        return bool(self.value)


class Number(Value):
    def __int__(self):
        return int(self.value)


