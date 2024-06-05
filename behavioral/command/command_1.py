"""
Command tem intenção de encapsular uma solicitação como
um objeto, desta forma permitindo parametrizar clientes com diferentes
solicitações, enfileirar ou fazer registro (log) de solicitações e suportar
operações que podem ser desfeitas.

É formado por um cliente (quem orquestra tudo), um invoker (que invoca as
solicitações), um ou vários objetos de comando (que fazem a ligação entre o
receiver e a ação a ser executada) e um receiver (o objeto que vai executar a
ação no final).
"""
from __future__ import annotations
from abc import abstractmethod, ABC


class Light:
    """ Receiver """

    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self) -> None:
        print(f'{self.name} no {self.room_name} está ON')

    def off(self) -> None:
        print(f'{self.name} no {self.room_name} está OFF')

    def change_color(self, color: str) -> None:
        self.color = color
        print(f'{self.name} no {self.room_name} está {self.color}')


class ICommand(ABC):
    ''' Interface de comando'''
    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass


class LightOnCommand(ICommand):
    ''' Comando concreto'''

    def __init__(self, light: Light) -> None:
        self.ligth = light

    def execute(self) -> None:
        self.ligth.on()

    def undo(self) -> None:
        self.ligth.off()


class LightChangeColor(ICommand):
    ''' Comando concreto'''

    def __init__(self, light: Light, color: str) -> None:
        self.ligth = light
        self.color = color
        self._old_color = self.ligth.color

    def execute(self) -> None:
        self._old_color = self.ligth.color
        self.ligth.change_color(self.color)

    def undo(self) -> None:
        self.ligth.change_color(self._old_color)


class RemoteController:
    ''' Invoker '''

    def __init__(self) -> None:
        self._buttons: dict[str, ICommand] = {}
        self._undos: list[tuple[str, str]] = []

    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_pressed(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
            self._undos.append((name, 'execute'))

    def button_undo(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.append((name, 'undo'))

    # Botão de desfazer global
    def global_undo(self) -> None:
        if not self._undos:
            print('Nothing to undo')
            return None
        button_name, action = self._undos[-1]
        if action == 'execute':
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()

        self._undos.pop()


if __name__ == '__main__':
    # Criando receivers
    bedroom_light = Light('Luz do quarto', 'Quarto')
    bathroom_light = Light('Luz do banheiro', 'Banheiro')

    # Criando comandos concretos
    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)
    bedroom_light_blue = LightChangeColor(bedroom_light, 'blue')
    bedroom_light_red = LightChangeColor(bedroom_light, 'red')

    # Criando o invoker
    remote = RemoteController()

    # Criando botões no invoker (setando comandos)
    remote.button_add_command('first_button', bedroom_light_on)
    remote.button_add_command('second_button', bathroom_light_on)
    remote.button_add_command('thirdy_button', bedroom_light_blue)
    remote.button_add_command('fourth_button', bedroom_light_red)

    # Pressionando os botões (executando os comandos)
    remote.button_pressed('first_button')
    remote.button_undo('first_button')

    remote.button_pressed('second_button')
    remote.button_undo('second_button')

    remote.button_pressed('thirdy_button')
    # remote.button_undo('thirdy_button')

    remote.button_pressed('fourth_button')
    remote.button_undo('fourth_button')

    print()

    # Desfazendo comandos
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
