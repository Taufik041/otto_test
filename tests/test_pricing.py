"""Pricing rules, straight from the pricing sheet in docs/PRICING.md."""

from inventory import pricing


def test_no_discount_below_threshold():
    # 9 units, no discount
    assert pricing.line_total(10.00, 9) == 90.00


def test_bulk_discount_at_exactly_ten_units():
    # The pricing sheet says TEN UNITS OR MORE qualifies: 100.00 - 10% = 90.00
    assert pricing.line_total(10.00, 10) == 90.00


def test_bulk_discount_above_threshold():
    assert pricing.line_total(10.00, 20) == 180.00


def test_negative_quantity_rejected():
    try:
        pricing.line_subtotal(5.0, -1)
    except ValueError:
        return
    raise AssertionError("expected ValueError")
