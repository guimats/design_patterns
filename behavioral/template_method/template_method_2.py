"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""
from abc import ABC, abstractmethod


class Pizza(ABC):
    """ Classe abstrata """

    def prepare(self) -> None:
        """ Template method """
        self.hook_before_add_ingredientes()
        self.add_ingredients()  # Abstract
        self.hook_after_add_ingredientes()
        self.cook()  # Abstract
        self.cut()  # Concretos
        self.server()  # Concretos

    def hook_before_add_ingredientes(self) -> None: pass
    def hook_after_add_ingredientes(self) -> None: pass

    def cut(self) -> None:
        print(f'{self.__class__.__name__}: cortando pizza')

    def server(self) -> None:
        print(f'{self.__class__.__name__}: servindo pizza')

    @abstractmethod
    def add_ingredients(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class AModa(Pizza):

    def add_ingredients(self) -> None:
        print('AModa: presunto, queijo, goiabada')

    def cook(self) -> None:
        print('AModa: cozinhando por 45 minutos no forno a lenha')


class Veg(Pizza):
    def hook_before_add_ingredientes(self) -> None:
        print('Veg: lavando ingredientes')

    def add_ingredients(self) -> None:
        print('Veg: ingredientes veganos')

    def cook(self) -> None:
        print('Veg: cozinhando por 5 minutos no forno comum')


if __name__ == '__main__':
    a_moda = AModa()
    a_moda.prepare()
    print()
    veg = Veg()
    veg.prepare()
