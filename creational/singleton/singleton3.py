# EXTRA DA AULA
# class Meta(type):
#     def __call__(self, *args, **kwargs):
#         print('CALL é executado')
#         return super().__call__(*args, **kwargs)


# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('NEW é executado')
#         return super().__new__(cls)

#     def __init__(self, nome) -> None:
#         print('INIT é executado')
#         self.nome = nome

#     # Permite que a instancia da classe possa ser chamada como função
#     # Ex:
#     # p1 = Pessoa()
#     # p1()
#     # Quando chamado, retorna o que está no método call
#     def __call__(self, x):
#         print('Call chamado', self.nome, x)


# p1 = Pessoa('Luiz')
# print(p1.nome)


class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        # O init é chamado toda as vezes
        self.tema = 'Tema escuro'
        self.font = '18px'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'Qualquer outra coisa'
    print(as1.tema)

    as2 = AppSettings()
    as3 = AppSettings()

    print(as2.tema)
    print(as3.tema)
