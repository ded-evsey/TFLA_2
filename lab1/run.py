"""Лабораторная работа No1
Тема "Машина Тьюринга".
1. Создать объекты программы реализующие машину Тьюринга.
2. Реализовать процедуры добавления/удаления переходов и состояний, добавления и
удаления начальных и заключительных состояний.
3. Реализовать процедуру перевода машины Тьюринга из заданного состояния в другое
посредством одного из допустимых переходов (т. е. Реализовать такт работы МТ).
4. Реализовать процедуру/метод работы детерминированной машины Тьюринга.
(20 баллов)
5. Реализовать с помощью машины Тьюринга распознавание строк вида «aaabbbccc» –
сначала символ a, потом столько же b и столько же c. (см. книгу Тома Стюарта)
(дополнительно 15 баллов)
6. Реализовать машину Тьюринга, реализующую вычисление квадратного корня из
натурального числа (см. лекцию 1 или Пентус стр. 61, пример 13.13).(дополнительно 15
баллов)
7. Реализовать универсальную машину Тьюринга. (дополнительно 15 баллов)
"""
__package__ = "lab1"
from .tape import Tape
from .tmrule import *
from .dtm import DTM, DTMRulebook
from .dtm_design import DTMDesign


def read_write_move(tape):
    print(tape)
    print(tape.move_head_left)
    print(tape.write('0'))
    print(tape.move_head_right)
    print(tape.move_head_right.write('0'))


def changing_state(rule):
    print(vars(rule))
    print(rule.applies_to(TMConfiguration(1, Tape([], '0', [], '_'))))
    print(rule.applies_to(TMConfiguration(1, Tape([], '1', [], '_'))))
    print(rule.applies_to(TMConfiguration(2, Tape([], '0', [], '_'))))
    print(rule.follow(TMConfiguration(1, Tape([], '0', [], '_'))).__dict__)


def create_mt(rulebook, tape):
    print(rulebook.__dict__)
    conf = TMConfiguration(1, tape)
    print(conf.__dict__)
    conf = rulebook.next_configuration(conf)
    print(conf.__dict__)
    conf = rulebook.next_configuration(conf)
    print(conf.__dict__)
    conf = rulebook.next_configuration(conf)
    print(conf.__dict__)


# Модель детерминирванной Машины Тьюринга
def dt_machine(tape, rulebook):
    dtm = DTM(TMConfiguration(1, tape), [3], rulebook)
    print(dtm)
    print(dtm.current_configuration.__dict__)
    print(dtm.accepting)
    dtm.step()
    print(dtm.current_configuration.__dict__)
    print(dtm.accepting)
    print(dtm.run())
    print(dtm.current_configuration.__dict__)
    print(dtm.accepting)


def resolve_stuck(rulebook):
    tape = Tape(['1', '2', '1'], '1', [], '_')
    print(tape)
    dtm = DTM(TMConfiguration(1, tape), [3], rulebook)

    print(dtm.run())
    print(dtm.current_configuration.__dict__)
    print(dtm.accepting)
    print(dtm.stuck)


def aaabbbccc():
    rulebook = DTMRulebook([
        TMRule(1, 'X', 1, 'X', RIGHT),
        TMRule(1, 'a', 2, 'X', RIGHT),
        TMRule(1, '_', 6, '_', LEFT),

        TMRule(2, 'a', 2, 'a', RIGHT),
        TMRule(2, 'X', 2, 'X', RIGHT),
        TMRule(2, 'b', 3, 'X', RIGHT),

        TMRule(3, 'b', 3, 'b', RIGHT),
        TMRule(3, 'X', 3, 'X', RIGHT),
        TMRule(3, 'c', 4, 'X', RIGHT),

        TMRule(4, 'c', 4, 'c', RIGHT),
        TMRule(4, '_', 5, '_', LEFT),

        TMRule(5, 'a', 5, 'a', LEFT),
        TMRule(5, 'b', 5, 'b', LEFT),
        TMRule(5, 'c', 5, 'c', LEFT),
        TMRule(5, 'X', 5, 'X', LEFT),
        TMRule(5, '_', 1, '_', RIGHT),
    ])

    tape = Tape([], 'a', ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'], '_')
    print(tape)
    dtm = DTM(TMConfiguration(1, tape), [6], rulebook)
    [dtm.step() for _ in range(10)]
    print(dtm.current_configuration)
    [dtm.step() for _ in range(25)]
    print(dtm.current_configuration)
    dtm.run()
    print(dtm.current_configuration)


def calc_square_root():
    rulebook = DTMRulebook([
        TMRule(1, '_', 2, '_', RIGHT),
        TMRule(2, '_', 7, '_', STAY),
        TMRule(2, 'a', 3, 'a', LEFT),

        TMRule(3, '_', 3, 'a', RIGHT),
        TMRule(3, 'a', 4, '_', RIGHT),

        TMRule(4, '_', 5, '_', LEFT),
        TMRule(4, 'a', 8, 'a', STAY),

        TMRule(5, '_', 6, '_', LEFT),
        TMRule(6, 'a', 6, 'a', LEFT),
        TMRule(6, '_', 7, '_', STAY),

        TMRule(8, '_', 8, '_', RIGHT),
        TMRule(8, 'a', 9, 'a', RIGHT),

        TMRule(9, 'a', 9, 'a', RIGHT),
        TMRule(9, '_', 10, '_', LEFT),

        TMRule(10, 'a', 11, '_', LEFT),
        TMRule(11, '_', 11, '_', STAY),
        TMRule(11, 'a', 12, '_', LEFT),

        TMRule(12, 'a', 12, 'a', LEFT),
        TMRule(12, '_', 13, '_', LEFT),

        TMRule(13, '_', 13, '_', LEFT),
        TMRule(13, 'a', 14, '_', LEFT),

        TMRule(14, 'a', 8, 'a', RIGHT),
        TMRule(14, '_', 3, '_', RIGHT),
    ])

    # Создание Универсальной Машины Тьюригна
    dtm_design = DTMDesign([7], rulebook)
    i, j, k = 0, 1, 2

    tape = Tape([], '_', ['a'] * (i + (j + 2) ** 2), '_')
    print(tape, 'count "a" == {0}'.format(len(tape.right)))
    print(dtm_design.accepts(tape))

    tape = Tape([], '_', ['a'] * (k + 2) ** 2, '_')
    print(tape, 'count "a" == {0}'.format(len(tape.right)))
    print(dtm_design.accepts(tape))


if __name__ == '__main__':
    tp = Tape(['1', '0', '1'], '1', [], '_')
    rl = TMRule(1, '0', 2, '1', RIGHT)
    # Создание объекта DTMRulebook для Машины Тьюринга по "инкременту двоичных чисел"
    rb = DTMRulebook([
        TMRule(1, '0', 2, '1', RIGHT),
        TMRule(1, '1', 1, '0', LEFT),
        TMRule(1, '_', 2, '1', RIGHT),
        TMRule(2, '0', 2, '0', RIGHT),
        TMRule(2, '1', 2, '1', RIGHT),
        TMRule(2, '_', 3, '_', LEFT),
    ])
    read_write_move(tp)
    changing_state(rl)
    create_mt(rb, tp)
    dt_machine(tp, rb)
    resolve_stuck(rb)
    aaabbbccc()
    calc_square_root()
