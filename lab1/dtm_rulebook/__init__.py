class DTMRulebook:
    def __init__(self, rules):
        self.rules = rules
        
    def next_configuration(self, configuration):
        conf = self.rule_for(configuration)
        if conf:
            return conf.follow(configuration)
    
    def rule_for(self, configuration):
        applies_to = lambda rule: rule.applies_to(configuration)
        rules = list(filter(applies_to, self.rules))
        try:
            return rules[0]
        except IndexError:
            return None

    def applies_to(self, configuration):
        return not self.rule_for(configuration) is None
