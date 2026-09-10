"""Shared configuration values for the inventory service.

Anything tunable lives here so the rest of the package never hardcodes numbers.
"""

# Orders of this many units or more qualify for the bulk discount.
BULK_THRESHOLD = 10

# Fraction taken off the line total once BULK_THRESHOLD is reached.
BULK_DISCOUNT_RATE = 0.10

# Applied after discounts, to the whole order.
TAX_RATE = 0.08

# Orders above this value ship free.
FREE_SHIPPING_OVER = 500.00

FLAT_SHIPPING_FEE = 12.50

# Maximum units of a single SKU allowed in one order.
MAX_UNITS_PER_LINE = 999

CURRENCY = "USD"
