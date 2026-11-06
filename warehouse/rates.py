"""Shipping rate calculations."""

_EXPRESS_SURCHARGE = 7.0


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Quote shipping in dollars.

    Args:
        weight_kg: Parcel weight; must be positive.
        zone: Delivery zone — ``"local"`` or ``"regional"``.
        service: Shipping service — ``"standard"`` (default) or ``"express"``.
            Express adds $7 to the standard rate for any zone.

    Returns:
        Quoted price in dollars, rounded to two decimal places.

    Raises:
        ValueError: If *weight_kg* is non-positive, *zone* is unknown, or
            *service* is not ``"standard"`` or ``"express"``.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in {"local", "regional"}:
        raise ValueError("unknown zone")
    if service not in {"standard", "express"}:
        raise ValueError(f"unknown service: {service!r}")
    base = 5.0 if zone == "local" else 8.0
    surcharge = _EXPRESS_SURCHARGE if service == "express" else 0.0
    return round(base + 1.5 * weight_kg + surcharge, 2)
