"""
O Padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    """ Context """

    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        print('Tentando executar pending()')
        self.state.pending()
        print(f'Estado atual: {self.state}')
        print()

    def approve(self) -> None:
        print('Tentando executar approve()')
        self.state.approve()
        print(f'Estado atual: {self.state}')
        print()

    def reject(self) -> None:
        print('Tentando executar reject()')
        self.state.reject()
        print(f'Estado atual: {self.state}')
        print()


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def approve(self) -> None: pass

    @abstractmethod
    def reject(self) -> None: pass

    def __str__(self) -> str:
        return self.__class__.__name__


class PaymentPending(OrderState):
    def pending(self) -> None:
        print('Pagamento já pendente. Não posso alterar')

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('Pagamento aprovado')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento recusado')


class PaymentApproved(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Pagamento pendente')

    def approve(self) -> None:
        print('Pagamento já aprovado. Não posso alterar')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento recusado')


class PaymentRejected(OrderState):
    def pending(self) -> None:
        print('Pagamento já recusado. Não posso alterar para pendente')

    def approve(self) -> None:
        print('Pagamento já recusado. Não posso alterar para aprovado')

    def reject(self) -> None:
        print(
            'Pagamento já recusado. Não posso alterar para recusado novamente'
        )


if __name__ == '__main__':
    order = Order()
    order.pending()
    order.approve()
    order.approve()
    order.reject()
    order.approve()
    order.reject()
