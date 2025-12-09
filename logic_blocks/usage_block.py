def generate_usage_block(product: dict) -> str:
    usage = product.get("how_to_use", "")
    if not usage:
        return "No usage instructions provided."
    return "How to Use: " + usage
