from logic_blocks.benefits_block import generate_benefits_block
from logic_blocks.usage_block import generate_usage_block
from logic_blocks.safety_block import generate_safety_block
from logic_blocks.price_block import generate_price_block
from logic_blocks.ingredients_block import generate_ingredients_block
from logic_blocks.comparison_block import compare_products
import json

class TemplateEngineAgent:
    """
    Agent to fill templates for Product, FAQ, and Comparison pages.
    """

    def generate_product_page(self, product: dict) -> dict:
        page = {
            "product_name": product.get("product_name", ""),
            "concentration": product.get("concentration", ""),
            "skin_type": product.get("skin_type", []),
            "ingredients_block": generate_ingredients_block(product),
            "benefits_block": generate_benefits_block(product),
            "usage_block": generate_usage_block(product),
            "safety_block": generate_safety_block(product),
            "price_block": generate_price_block(product)
        }
        return page

    def generate_comparison_page(self, product_a: dict, product_b: dict) -> dict:
        return compare_products(product_a, product_b)

    def generate_faq_page(self, questions: dict) -> dict:
        """
        questions: dict with categories as keys and list of questions as values
        """
        faq_list = []
        for category, qs in questions.items():
            for q in qs:
                faq_list.append({"category": category, "question": q})
        return {"faqs": faq_list}

    def save_json(self, data: dict, filename: str):
        with open(f"outputs/{filename}", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
