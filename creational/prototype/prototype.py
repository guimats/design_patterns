"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo
"""
from __future__ import annotations
from copy import deepcopy


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k} = {v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.address: list[Address] = []

    def add_address(self, address: Address) -> None:
        self.address.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == '__main__':
    luiz = Person('Luiz', 'Miranda')
    luiz_address = Address('Av Brasil', '250A')
    luiz.add_address(luiz_address)

    esposa_luiz = luiz.clone()
    esposa_luiz.firstname = 'Leticia'

print(luiz)
print(esposa_luiz)
