from comprehensions.DomainObjects import Order


def get_order_details(order: Order, mask_phone: bool = False):
    return {
        "name": order.customer.name,
        "phone": mask_phone_number(order) if mask_phone else order.customer.phone,
        "amount": order.total_amount,
        "qty": sum([detail.quantity for detail in order.details]),
    }


# mask the customer phone number: xxx-xxx-nnnn
def mask_phone_number(
    order: Order,
):
    return f"xxx-xxx-{order.customer.phone[8:]}"
