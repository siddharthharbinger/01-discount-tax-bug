from decimal import Decimal


def checkout_total(subtotal: Decimal, discount_rate: Decimal, tax_rate: Decimal) -> Decimal:
    """Return the final checkout total after discount and tax."""
    # Calculate discount amount
    discount = subtotal * discount_rate
    # Subtotal after discount
    subtotal_after_discount = subtotal - discount
    # Tax should be applied to the discounted subtotal, not the original subtotal
    tax = subtotal_after_discount * tax_rate
    # Final total is discounted subtotal plus tax, rounded to two decimal places
    return (subtotal_after_discount + tax).quantize(Decimal("0.01"))
