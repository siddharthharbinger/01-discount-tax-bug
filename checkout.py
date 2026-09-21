from decimal import Decimal


def checkout_total(subtotal: Decimal, discount_rate: Decimal, tax_rate: Decimal) -> Decimal:
    """Return the final checkout total after discount and tax.

    The discount is applied first, and tax is calculated on the discounted amount.
    The final total is rounded to two decimal places.
    """
    # Amount reduced by the discount
    discount = subtotal * discount_rate
    discounted_subtotal = subtotal - discount

    # Tax should be applied to the discounted subtotal, not the original subtotal
    tax = discounted_subtotal * tax_rate

    # Final total = discounted subtotal + tax, rounded to cents
    return (discounted_subtotal + tax).quantize(Decimal("0.01"))
