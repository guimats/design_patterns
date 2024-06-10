"""
O Proxy é um padrão de projeto estrutural que tem a
intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o código cliente
gostaria de usar.
O proxy receberá as solicitações e terá controle
sobre como e quando repassar tais solicitações ao
objeto real.

Com base no modo como o proxies são usados,
nós os classificamos como:

- Proxy Virtual: controla acesso a recursos que podem
ser caros para criação ou utilização.
- Proxy Remoto: controla acesso a recursos que estão
em servidores remotos.
- Proxy de proteção: controla acesso a recursos que
possam necessitar autenticação ou permissão.
- Proxy inteligente: além de controlar acesso ao
objeto real, também executa tarefas adicionais para
saber quando e como executar determinadas ações.

Proxies podem fazer várias coisas diferentes:
criar logs, autenticar usuários, distribuir serviços,
criar cache, criar e destruir objetos, adiar execuções
e muito mais...
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep


class IUser(ABC):
    """ Subject Interface """

    first_name: str
    last_name: str

    @abstractmethod
    def get_addresses(self) -> list[dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> dict: pass


class RealUser(IUser):
    """ Reak Subject """

    def __init__(self, first_name: str, last_name: str) -> None:
        sleep(2)  # Simulando requisição
        self.first_name = first_name
        self.last_name = last_name

    def get_addresses(self) -> list[dict]:
        sleep(2)  # Simulando requisição
        return [
            {'rua': 'Av. Brasil', 'numero': 500}
        ]

    def get_all_user_data(self) -> dict:
        sleep(2)  # Simulando requisição
        return {'cpf': '111.111.111-11', 'rg': '264881570'}


class UserProxy(IUser):
    """ Proxy """

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self._real_user: RealUser

        # Esses objetos ainda não existem nesse ponto do código
        self._cached_addresses: list[dict]
        self._all_user_data: dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.first_name, self.last_name)

    def get_addresses(self) -> list[dict]:
        self.get_real_user()
        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()
        return self._cached_addresses

    def get_all_user_data(self) -> dict:
        self.get_real_user()
        if not hasattr(self, '_cached_addresses'):
            self._all_user_data = self._real_user.get_all_user_data()
        return self._all_user_data


if __name__ == "__main__":
    luiz = UserProxy('Luiz', 'Otavio')

    print(luiz.first_name)
    print(luiz.last_name)

    # 6 segundos para responder
    print(luiz.get_all_user_data())
    print(luiz.get_addresses())

    # responde instantaneamente
    print('Cached data')
    for i in range(50):
        print(luiz.get_addresses())
