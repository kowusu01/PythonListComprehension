from typing import List
from comprehensions.DomainObjects import Order

def order_min_amount(order: Order, min_order_total: int) -> bool:
    """
    implement some complex business logic here
    Args:
        - order: Order - the order to order meets the minimum amount
        - minOrderTotal: int - the minimum order total to be considered
    """
    return order.total_amount >= min_order_total


def order_min_quantity(order: Order, min_order_qty: int) -> bool:
    """
    implement some complex business logic here
    Args:
        - order: Order - the order to if the order meets the minimum quantity
        - minOrderQty: int - the minimum order items to be considered
    """
    return sum([detail.quantity for detail in order.details]) >= min_order_qty


def from_one_of_cities(order: Order, cities: List[str]) -> bool:
    """
    implement some complex business logic here
    Args:
        - order: Order - the order to if from one of the cities indicated
        - cities: List[str] - the list of cities to check if the order is from
    """
    return order.customer.city in cities
