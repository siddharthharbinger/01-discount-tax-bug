from decimal import Decimal


def checkout_total(subtotal: Decimal, discount_rate: Decimal, tax_rate: Decimal) -> Decimal:
    """Return the final checkout total after discount and tax.

    The discount is applied first, then tax is calculated on the discounted
    amount. The result is rounded to two decimal places.
    """
    # Calculate the discount amount.
    discount = subtotal * discount_rate
    # Subtotal after discount.
    discounted_subtotal = subtotal - discount
    # Tax should be applied to the discounted subtotal, not the original.
    tax = discounted_subtotal * tax_rate
    # Final total, rounded to cents.
    return (discounted_subtotal + tax).quantize(Decimal("0.01"))
