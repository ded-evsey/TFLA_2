from simple_lang.types import Number, Boolean
from simple_lang.units import Sequence, Variable
from simple_lang.operations import (
    Add,
    Subtraction,
    Division,
    Multiply,
    Less,
    More,
    And,
    Or,
    Not
)
from simple_lang.operators import (
    DoNothing,
    Assign,
    If,
    While
)
from simple_lang import SimpleMachine


def task_2():
    """
        Задание 2: Реализовать алгоритм мелких шагов сворачивания
        для синтаксического дерева,
        представленного одним объектом
        на примере простых арифметических выражений.
        (см.книгу Тома Стюарта)
    """
    exp = Multiply(
        Add(
            Subtraction(
                Number(3),
                Number(4)
            ),
            Number(2)
        ),
        Division(
            Number(6), Number(2)
        )
    )
    sm = SimpleMachine(exp)
    sm.run()
    print(sm.history)


def task_3():
    """
        Задание 3: Реализовать алгоритм семантики мелких шагов
         для вычисления алгебраических выражений
    """
    exp = Or(
        And(
            Less(
                Multiply(
                    Add(
                        Subtraction(
                            Number(3),
                            Number(4)
                        ),
                        Number(2)
                    ),
                    Division(
                        Number(6),
                        Number(2)
                    )
                ),
                Number(4)
            ),
            Not(
                More(
                    Variable('x'),
                    Variable('y')
                )
            )
        ),
        Boolean(True)
    )
    env = {
        'x': Number(11),
        'y': Number(2)
    }
    sm = SimpleMachine(exp, env)
    sm.run()
    print(sm.history)


def task_4():
    """
        Задание 4: Реализовать алгоритм семантики мелких шагов
        для операторов языка программирования:
        присваивание, условный оператор, оператор цикла
    """
    stat = If(
        Less(
            Number(4),
            Add(
                Number(4),
                Number(1)
            )
        ),
        While(
            Less(
                Variable('x'),
                Number(5)
            ),
            Assign(
                'x',
                Multiply(
                    Variable('x'),
                    Number('3')
                )
            )
        ),
        Sequence(
            Assign(
                'x',
                Add(
                    Number(1),
                    Number(5)
                )
            ),
            Assign(
                'y',
                Add(
                    Variable('x'),
                    Number(3)
                )
            )
        )
    )
    env = {'x': Number(1)}
    sm = SimpleMachine(
        stat,
        env
    )
    sm.run()
    print(sm.history)


if __name__ == "__main__":
    task_2()
    task_3()
    task_4()
