class Customer:
    def __init__(
        self, id, name, city, email, phone
    ):
        self.id = id
        self.name = name
        self.city = city
        self.email = email
        self.phone = phone


class Order:
    def __init__(
        self,
        id,
        order_date,
        total_amount,
        customer,
        details,
        expected_ship_date,
        actual_ship_date,
    ):
        self.id = id
        self.order_date = order_date
        self.total_amount = total_amount
        self.customer = customer
        self.details = details
        self.expected_ship_date = expected_ship_date
        self.actual_ship_date = actual_ship_date


class OrderDetail:
    def __init__(self, id, product_name, price, quantity):
        self.detail_id = id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
