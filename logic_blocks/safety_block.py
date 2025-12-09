def generate_safety_block(product: dict) -> str:
    """
    Returns formatted safety / side effects information.
    """
    safety = product.get("side_effects", "")
    if not safety:
        return "No safety information provided."
    return "Safety: " + safety
