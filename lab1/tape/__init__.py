class Tape:
    """Класс чисто функциональный, т.е. запись на ленту и сдвиг головки - недеструктивные операции"""
    def __init__(self, left: list, middle: str, right: list, blank):
        self.left = left
        self.middle = middle
        self.right = right
        self.blank = blank

    """Операции для записи символа в текущую ячейку и сдвига головки влево и вправо"""
    def write(self, character):
        return Tape(self.left, character, self.right, self.blank)

    @property
    def move_head_left(self):
        middle = self.left[-1:] or self.blank
        return Tape(self.left[:-1], "".join(middle), [self.middle] + self.right, self.blank)

    @property
    def move_head_right(self):
        middle = self.right[:1] or self.blank
        return Tape(self.left + [self.middle], "".join(middle), self.right[1:], self.blank)

    def __repr__(self):
        return "#<Tape {0}({1}){2}>".format("".join(self.left), self.middle, "".join(self.right))