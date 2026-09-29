"""Order assembly and totals."""

from __future__ import annotations

from dataclasses import dataclass, field

from . import pricing


@dataclass
class OrderLine:
    sku: str
    unit_price: float
    quantity: int

    def total(self) -> float:
        return pricing.line_total(self.unit_price, self.quantity)


@dataclass
class Order:
    order_id: str
    lines: list[OrderLine] = field(default_factory=list)

    def add_line(self, sku: str, unit_price: float, quantity: int) -> OrderLine:
        line = OrderLine(sku=sku, unit_price=unit_price, quantity=quantity)
        self.lines.append(line)
        return line

    def subtotal(self) -> float:
        return round(sum(line.total() for line in self.lines), 2)

    def shipping(self) -> float:
        return pricing.shipping_fee(self.subtotal())

    def total(self) -> float:
        """Grand total: discounted lines, plus shipping, plus tax."""
        return pricing.with_tax(self.subtotal() + self.shipping())

    def unit_count(self) -> int:
        return sum(line.quantity for line in self.lines)

    def line_count(self) -> int:
        return len(self.lines)
