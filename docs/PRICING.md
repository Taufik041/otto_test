# Pricing sheet (authoritative)

These are the rules Finance signs off on. Code must match this document.

## Bulk discount

An order line of **ten units or more** receives a **10%** discount on that
line's subtotal. Nine units receives no discount. Ten units receives the
discount.

> Wording note: an earlier version of this sheet said "more than ten units",
> which was corrected in the 0.4.0 revision. Some code may still implement the
> old wording.

## Tax

8% sales tax applies to the order total after discounts and shipping.

## Shipping

Flat 12.50 fee, waived for orders of 500.00 or more (inclusive).

## Legacy rules

The pre-2019 rules (25 unit threshold, 5% discount) live in
`legacy_pricing.py` and are frozen for historical reporting. They must not be
changed to match this sheet.
