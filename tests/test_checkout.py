from decimal import Decimal

from checkout import checkout_total


def test_tax_is_calculated_after_discount():
    assert checkout_total(Decimal("100.00"), Decimal("0.20"), Decimal("0.10")) == Decimal("88.00")
