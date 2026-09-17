from decimal import Decimal


def checkout_total(subtotal: Decimal, discount_rate: Decimal, tax_rate: Decimal) -> Decimal:
    """Return the final checkout total after discount and tax."""
    discount = subtotal * discount_rate
    tax = subtotal * tax_rate
    return (subtotal - discount + tax).quantize(Decimal("0.01"))
