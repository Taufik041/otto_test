"""Price calculation for order lines.

This is the module the rest of the system should be using. See
``legacy_pricing`` for the pre-2019 implementation that is still imported by a
couple of reporting scripts.
"""

from __future__ import annotations

from . import config


def line_subtotal(unit_price: float, quantity: int) -> float:
    """Price for a line before any discount is applied."""
    if quantity < 0:
        raise ValueError("quantity cannot be negative")
    if quantity > config.MAX_UNITS_PER_LINE:
        raise ValueError(f"quantity exceeds {config.MAX_UNITS_PER_LINE}")
    return round(unit_price * quantity, 2)


def qualifies_for_bulk(quantity: int) -> bool:
    """Whether a line of ``quantity`` units gets the bulk discount.

    The rule from the pricing sheet: ten units or more qualifies.
    """
    return quantity >= config.BULK_THRESHOLD


def apply_discount(subtotal: float, quantity: int) -> float:
    """Apply the bulk discount to a line subtotal, if it qualifies."""
    if not qualifies_for_bulk(quantity):
        return subtotal
    return round(subtotal * (1 - config.BULK_DISCOUNT_RATE), 2)


def line_total(unit_price: float, quantity: int) -> float:
    """Final price for a single order line."""
    return apply_discount(line_subtotal(unit_price, quantity), quantity)


def shipping_fee(order_value: float) -> float:
    """Flat fee unless the order is large enough to ship free."""
    if order_value >= config.FREE_SHIPPING_OVER:
        return 0.0
    return config.FLAT_SHIPPING_FEE


def with_tax(amount: float) -> float:
    """Add sales tax to an amount."""
    return round(amount * (1 + config.TAX_RATE), 2)
