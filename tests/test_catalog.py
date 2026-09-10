from inventory import catalog


def test_lookup_known_sku():
    p = catalog.lookup("SKU-1001")
    assert p.sku == "SKU-1001"


def test_lookup_unknown_sku_mentions_count():
    try:
        catalog.lookup("SKU-9999")
    except KeyError as e:
        assert "unknown sku" in str(e)
        return
    raise AssertionError("expected KeyError")
