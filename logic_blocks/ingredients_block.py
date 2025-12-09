def generate_ingredients_block(product: dict) -> str:
    """
    Returns formatted key ingredients information.
    """
    ingredients = product.get("key_ingredients", [])
    if not ingredients:
        return "Ingredients not listed."
    return "Key Ingredients: " + ", ".join(ingredients)
