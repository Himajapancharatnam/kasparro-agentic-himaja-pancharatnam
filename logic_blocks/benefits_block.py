def generate_benefits_block(product: dict) -> str:
    """
    Takes product dictionary and returns a formatted
    benefits string for templates.
    """
    benefits = product.get("benefits", [])
    if not benefits:
        return "No benefits listed."

    # Join benefits nicely
    return "Benefits: " + ", ".join(benefits)
