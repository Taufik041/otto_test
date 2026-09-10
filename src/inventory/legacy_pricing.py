"""DEPRECATED pre-2019 pricing rules.

Kept alive because ``scripts/quarterly_report.py`` still imports it. Do not use
for new code and do not "fix" the rules here to match the current pricing
sheet -- historical reports must keep reproducing historical numbers.
"""

from __future__ import annotations

# The old flat threshold, before config.py existed.
OLD_BULK_THRESHOLD = 25
OLD_BULK_DISCOUNT_RATE = 0.05


def qualifies_for_bulk(quantity: int) -> bool:
    """Pre-2019 rule: more than 25 units."""
    return quantity > OLD_BULK_THRESHOLD


def apply_discount(subtotal: float, quantity: int) -> float:
    """Pre-2019 discount. Frozen on purpose."""
    if not qualifies_for_bulk(quantity):
        return subtotal
    return round(subtotal * (1 - OLD_BULK_DISCOUNT_RATE), 2)


def line_total(unit_price: float, quantity: int) -> float:
    return apply_discount(round(unit_price * quantity, 2), quantity)
