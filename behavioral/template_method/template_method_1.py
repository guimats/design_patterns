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


class Absctract(ABC):
    def template_method(self) -> None:
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    def hook(self): pass

    def base_class_method(self) -> None:
        print('Olá, eu sou da classe abstrata')

    @abstractmethod
    def operation1(self) -> None: pass

    @abstractmethod
    def operation2(self) -> None: pass


class ConcreteClass1(Absctract):

    def hook(self):
        print('Eu vou utilizar o hook')

    def operation1(self) -> None:
        print('Operação 1 concluída')

    def operation2(self) -> None:
        print('Operação 2 concluída')


class ConcreteClass2(Absctract):

    def operation1(self) -> None:
        print('Operação 1 concluída (maneira diferente)')

    def operation2(self) -> None:
        print('Operação 2 concluída (maneira diferente)')


if __name__ == '__main__':
    c1 = ConcreteClass1()
    c1.template_method()

    print()

    c2 = ConcreteClass2()
    c2.template_method()
