"""
Builder é um padrão de criação que tem a intenção
de separar a construção de um objeto complexo
da sua representação, de modo que o mesmo processo
de construção possa criar diferentes representações.

Builder te da a possibilidade de criar objetos passo-a-passo
e isso já é possível no Python sem este padrão.

Geralmente o builder aceita o encadeamento de métodos
(method chaining).
"""
from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k} = {v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class User(StringReprMixin):
    def __init__(self) -> None:
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone: list = []
        self.address: list = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): pass

    @abstractmethod
    def add_fistname(self, firstname): pass

    @abstractmethod
    def add_lastname(self, lastname): pass

    @abstractmethod
    def add_age(self, age): pass

    @abstractmethod
    def add_phone(self, phone): pass

    @abstractmethod
    def add_address(self, address): pass


class UserBuilder(IUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def add_fistname(self, firstname):
        self._result.firstname = firstname
        return self

    def add_lastname(self, lastname):
        self._result.lastname = lastname
        return self

    def add_age(self, age):
        self._result.age = age
        return self

    def add_phone(self, phone):
        self._result.phone.append(phone)
        return self

    def add_address(self, address):
        self._result.address.append(address)
        return self


class UserDirector:
    def __init__(self, builder: UserBuilder):
        self._builder = builder

    def with_age(self, fisrtname, lastname, age):
        self._builder.add_fistname(fisrtname)
        self._builder.add_lastname(lastname)
        self._builder.add_age(age)
        return self._builder.result

    # Com encadeamento de método (não precisa chamar self._builder toda vez)
    def with_address(self, fisrtname, lastname, address):
        self._builder.add_fistname(fisrtname).add_lastname(
            lastname).add_address(address)
        return self._builder.result


if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age('Luiz', 'Otavio', 38)
    user2 = user_director.with_address('Maria', 'Miranda', 'Av Brasil')
    print(user1)
    print(user2)
