
from comprehensions.DomainObjects import Customer, Order, OrderDetail
from comprehensions.transformations import get_order_details
from comprehensions.filters import order_min_amount, from_one_of_cities, order_min_quantity


if __name__ == "__main__":
    
    # create three Customers
    customer1 = Customer(1, "Sara May", "New York", "sara.may@ai.com", "123-456-7890")
    customer2 = Customer(
        2, "John Doe", "San Antonio", "John.doe@arts.com", "098-765-4321"
    )
    customer3 = Customer(
        3, "Anette Barr", "Boston", "anette.barr@abc.com", "345-678-9012"
    )
    customer4 = Customer(
        1, "Nate Sam", "New York", "nate.sam@gmail.com", "145-674-8075"
    )

    # create some details
    detail1 = OrderDetail(1, "Laptop", 1299.99, 1)
    detail2 = OrderDetail(2, "Mouse", 20.95, 1)
    detail3 = OrderDetail(3, "Monitor", 199.99, 1)
    detail4 = OrderDetail(4, "Keyboard", 49.99, 1)
    detail5 = OrderDetail(5, "Cables", 4.95, 1)
    detail6 = OrderDetail(6, "Mouse", 41.90, 2)

    # create some orders using the details and customers
    order1 = Order(
        id=1,
        order_date="2021-01-01",
        total_amount=1520.93,
        customer=customer1,
        details=[detail1, detail2, detail3],
        expected_ship_date="2021-01-05",
        actual_ship_date="2021-01-01",
    )

    order2 = Order(
        id=2,
        order_date="2021-01-02",
        total_amount=54.94,
        customer=customer2,
        details=[detail4, detail5],
        expected_ship_date="2021-01-06",
        actual_ship_date="2021-01-07",
    )

    order3 = Order(
        id=3,
        order_date="2021-01-03",
        total_amount=1520.93,
        customer=customer3,
        details=[detail2, detail5],
        expected_ship_date="2021-01-07",
        actual_ship_date="2021-01-08",
    )

    order4 = Order(
        id=4,
        order_date="2021-01-04",
        total_amount=62.85,
        customer=customer4,
        details=[detail2, detail6],
        expected_ship_date="2021-01-05",
        actual_ship_date=None,
    )

    # 1. simple comprehension to get order totals
    print("\n1. simple comprehension to get order totals")
    orders = [order1, order2, order3, order4]
    totals = [order.total_amount for order in orders]
    print(totals)

    # 2. get customer name, total amount, and number_of_items for each order.
    print("\n2. name, total amount, and number_of_items for each order")
    order_details = [
        {
            "name": order.customer.name,
            "amount": order.total_amount,
            "qty": sum([detail.quantity for detail in order.details]),
        }
        for order in orders
    ]
    print(order_details)


# 3. abstract the comprehension into a function
print("\n3. Abstracting the comprehension into a function")
order_details = [get_order_details(order) for order in orders]
print(order_details)


# 4. Lets add a filter condition to the expression.
# We want to get the same order details but those that have more than 2 items.
order_details = [
    get_order_details(order)
    for order in orders
    if sum([detail.quantity for detail in order.details]) > 2
]

print("\n4. Order details with more than 2 items")
print(order_details)

# 5. lets extract the filter condition into a function
order_details = [
    get_order_details(order) for order in orders if order_min_quantity(order, 2)
]


# 6. lets add a min order amount as a condition
print("\n6. Order details with total amount greater than 1000")
order_details = order_details = [
    get_order_details(order) for order in orders if order_min_amount(order, 1000.00)
]
print(order_details)

# 7. add city filter condition and apply it with the min order amount
# customer from New York with order amount greater than 1000
print("\n7. Order details with total amount greater than 1000 and from New York")
order_details = [
    get_order_details(order)
    for order in orders
    if from_one_of_cities(order, ["New York"]) and order_min_amount(order, 100.00)
]
print(order_details)

# 8. lets add a transformation to mask the phone number
# the mask is added to the transformations and called when we get order details
# no need to change the comprehension
print("\n8. Masking the phone number")
order_details = [
    get_order_details(order, mask_phone=True)
    for order in orders
    if from_one_of_cities(order, ["New York"]) and order_min_amount(order, 50.00)
]
print(order_details)
