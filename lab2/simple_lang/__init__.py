class SimpleMachine:
    def __init__(self, statement=object(), environment=object()):
        self.statement = statement
        self.environment = environment
        self.history = []

    def update_history(self):
        self.history.append(self.statement.__str__())

    def step(self):
        try:
            statement, environment = self.statement.reduce(self.environment).values()
        except (TypeError, AttributeError):
            statement = self.statement.reduce(self.environment)
            environment = self.environment
        if not statement and not environment:
            self.statement = statement
        else:
            self.statement = statement
            self.environment = environment

    def run(self):
        while self.statement.reducible:
            self.update_history()
            self.step()
        self.update_history()
