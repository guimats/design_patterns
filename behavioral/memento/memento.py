"""
GoF - Memento é um padrão de projeto comportamental
que tem a intenção de permitir que você salve e restaure
um estado anterior de um objeto originator sem revelar os
detalhes da sua implementação e sem violar o encapsulamento.

Originator é o objeto que deseja salvar seu estado.
Memento é usado para salvar o estado do Originator.
Caretaker é usado para armazenar mementos.
Caretaker também é usado com o Padrão Command.
"""
from __future__ import annotations
from copy import deepcopy
from typing import Any


class Memento:
    def __init__(self, state: dict) -> None:
        self._state: dict
        super().__setattr__('_state', state)

    def get_state(self) -> dict:
        return self._state

    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError('Sorry, I am immutable')


class ImageEditor:
    def __init__(self, name: str, width: int, heigth: int) -> None:
        self.name = name
        self.width = width
        self.heigth = heigth

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()

    def __str__(self) -> str:
        return f'{self.__class__.__name__})({self.__dict__})'


class Caretaker:
    def __init__(self, originator: ImageEditor) -> None:
        self._originator = originator
        self._mementos: list[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:
        if not self._mementos:
            return

        # pop retorna o ultimo memento salvo e restaura no originator
        self._originator.restore(self._mementos.pop())


if __name__ == "__main__":
    img = ImageEditor('FOTO_1.jpg', 111, 111)
    caretaker = Caretaker(img)

    caretaker.backup()

    img.name = 'FOTO_2.jpg'
    img.width = 222
    img.heigth = 222
    caretaker.backup()

    img.name = 'FOTO_3.jpg'
    img.width = 333
    img.heigth = 333
    caretaker.backup()

    img.name = 'FOTO_4.jpg'
    img.width = 444
    img.heigth = 444

    caretaker.restore()

    print(img)
