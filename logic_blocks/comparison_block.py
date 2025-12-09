def compare_products(product_a: dict, product_b: dict) -> dict:
    """
    Compares two products and returns a structured dict.
    """
    comparison = {
        "product_a": {
            "name": product_a.get("product_name", ""),
            "benefits": product_a.get("benefits", []),
            "price": product_a.get("price", "")
        },
        "product_b": {
            "name": product_b.get("product_name", ""),
            "benefits": product_b.get("benefits", []),
            "price": product_b.get("price", "")
        }
    }
    return comparison
