from decimal import Decimal


def checkout_total(subtotal: Decimal, discount_rate: Decimal, tax_rate: Decimal) -> Decimal:
    """Return the final checkout total after discount and tax."""
    # Calculate the discount amount.
    discount = subtotal * discount_rate
    # Apply discount first, then compute tax on the discounted subtotal.
    discounted_subtotal = subtotal - discount
    tax = discounted_subtotal * tax_rate
    # Return the final amount, rounded to two decimal places.
    return (discounted_subtotal + tax).quantize(Decimal("0.01"))
