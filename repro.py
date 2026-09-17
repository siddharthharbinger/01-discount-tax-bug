from decimal import Decimal

from checkout import checkout_total


actual = checkout_total(Decimal("100.00"), Decimal("0.20"), Decimal("0.10"))
expected = Decimal("88.00")
print(f"actual={actual} expected={expected}")
raise SystemExit(0 if actual == expected else 1)
