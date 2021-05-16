RIGHT = 1
LEFT = -1
STAY = 0

class TMConfiguration:
    """ Конфигурация Машины Тьбюринга -
    это комбинация состояния и ленты
    """
    def __init__(self, state, tape):
        self.state = state
        self.tape = tape

    def __repr__(self):
        return "#<TMConfiguration state: {0} tape: {1}".format(self.state, self.tape)


class TMRule:
    def __init__(self, state, character, next_state, write_character, direction):
        self.state = state
        self.character = character
        self.next_state = next_state
        self.write_character = write_character
        self.direction = direction

    def applies_to(self, configuration: TMConfiguration):
        """Правило применимо только тогда, когда текущее состояние машины и символ под головкой
        совпадают с ожидаемыми"""
        return self.state == configuration.state and self.character == configuration.tape.middle

    def follow(self, configuration):
        """Обновление конфигурации путем изменения состояния машины в соответсвии с выбранным правилом"""
        return TMConfiguration(self.next_state, self.next_tape(configuration))

    def next_tape(self, configuration):
        writtern_tape = configuration.tape.write(self.write_character)
        if self.direction == LEFT:
            return writtern_tape.move_head_left
        if self.direction == RIGHT:
            return writtern_tape.move_head_right
        if self.direction == STAY:
            return writtern_tape.move_head_left.move_head_right