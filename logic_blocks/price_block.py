def generate_price_block(product: dict) -> str:
    """
    Returns formatted price information.
    """
    price = product.get("price", "")
    if not price:
        return "Price not available."
    return "Price: " + str(price)
