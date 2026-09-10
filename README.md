# inventory

A small order-pricing service. Nothing here is exciting; it exists to be
maintained.

```
src/inventory/
  config.py           tunable constants (thresholds, rates, fees)
  pricing.py          current pricing rules -- use this
  legacy_pricing.py   frozen pre-2019 rules -- do not modify
  orders.py           Order / OrderLine assembly
  catalog.py          generated product catalogue (long)
tests/
docs/
```

## Running the tests

```
pip install -e .
python -m pytest -q
```

## Known state

Two tests are failing after the 0.4.1 threshold refactor. See `docs/PRICING.md`
for the rules they are checking against.
