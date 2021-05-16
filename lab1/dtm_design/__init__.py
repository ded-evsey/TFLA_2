from ..dtm import DTM, DTMRulebook
from ..tmrule import TMConfiguration

class DTMDesign:
    def __init__(self, accept_states: list, rulebook: DTMRulebook):
        self.accept_states = accept_states
        self.rulebook = rulebook

    def accepts(self, tape):
        config = TMConfiguration(1, tape)
        dtm = self.to_dtm(config)
        dtm.run()
        return dtm.current_configuration

    def to_dtm(self, configuration):
        return DTM(configuration, self.accept_states, self.rulebook)