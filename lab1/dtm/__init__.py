from ..dtm_rulebook import DTMRulebook

class DTM:
    def __init__(self, current_configuration, accept_states: list, rulebook: DTMRulebook):
        self.current_configuration = current_configuration
        self.accept_states = accept_states
        self.rulebook = rulebook

    @property
    def accepting(self):
        return {self.current_configuration.state}.issubset(self.accept_states)
    
    def step(self):
        self.current_configuration = self.rulebook.next_configuration(self.current_configuration)
        return self.current_configuration

    @property
    def stuck(self):
        return not self.accepting and not self.rulebook.applies_to(self.current_configuration)
    
    def run(self):
        while not (self.accepting | self.stuck):
            self.step()


