"""Order totals end to end."""

from inventory.orders import Order


def test_small_order_pays_shipping():
    o = Order(order_id="A-1")
    o.add_line("SKU-1001", 25.00, 2)
    # 50.00 subtotal + 12.50 shipping = 62.50, +8% tax
    assert o.total() == 67.50


def test_bulk_order_gets_line_discount():
    o = Order(order_id="A-2")
    o.add_line("SKU-1002", 20.00, 10)
    # 200.00 - 10% bulk = 180.00, + 12.50 shipping = 192.50, +8% tax
    assert o.subtotal() == 180.00
    assert o.total() == 207.90


def test_unit_count():
    o = Order(order_id="A-3")
    o.add_line("SKU-1003", 5.00, 3)
    o.add_line("SKU-1004", 5.00, 4)
    assert o.unit_count() == 7
