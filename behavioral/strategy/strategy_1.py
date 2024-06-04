"""
Strategy é um padrão de projeto comportamental que tem
a intenção de definir uma família de algoritmos,
encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algorítmo varie independentemente
dos clientes que o utilizam.

Princípio do aberto/fechado (Open/closed principle)
Entidades devem ser abertas para extensão, mas fechadas para modificação
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self, total: float, discount: DiscountStrategy) -> None:
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass


class TwentyPercente(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value-(value * 0.2)


class FiftyPercente(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value-(value * 0.5)


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount):
        self.discount = discount/100

    def calculate(self, value: float) -> float:
        return value-(value * self.discount)


if __name__ == '__main__':
    twenty_percent = TwentyPercente()
    fifty_percent = FiftyPercente()
    no_discount = NoDiscount()
    five_percent = CustomDiscount(5)

    order = Order(1000, twenty_percent)
    print(order.total, order.total_with_discount)

    order2 = Order(1000, fifty_percent)
    print(order2.total, order2.total_with_discount)

    order3 = Order(1000, no_discount)
    print(order3.total, order3.total_with_discount)

    order4 = Order(1000, five_percent)
    print(order4.total, order4.total_with_discount)

    order4 = Order(1000, CustomDiscount(13))
    print(order4.total, order4.total_with_discount)
