# Discount and Tax Bug

High-level bug: `checkout_total` applies tax to the pre-discount subtotal. The expected behavior is to apply the discount first, then calculate tax on the discounted amount.

Run the reproduction with:

```powershell
python repro.py
```

Run the failing test with:

```powershell
python -m pytest -q
```

Expected result: `checkout_total(100.00, 0.20, 0.10)` should return `88.00`, but the buggy implementation returns `90.00`.
