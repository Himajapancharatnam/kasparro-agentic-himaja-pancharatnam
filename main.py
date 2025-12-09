from orchestrator.pipeline import run_pipeline
from logic_blocks.benefits_block import generate_benefits_block
from logic_blocks.usage_block import generate_usage_block
from logic_blocks.safety_block import generate_safety_block
from logic_blocks.price_block import generate_price_block
from logic_blocks.ingredients_block import generate_ingredients_block
from logic_blocks.comparison_block import compare_products
from agents.template_engine import TemplateEngineAgent
import os

# Raw product data
product_data = {
    "Product Name": "GlowBoost Vitamin C Serum",
    "Concentration": "10% Vitamin C",
    "Skin Type": ["Oily", "Combination"],
    "Key Ingredients": ["Vitamin C", "Hyaluronic Acid"],
    "Benefits": ["Brightening", "Fades dark spots"],
    "How to Use": "Apply 2–3 drops in the morning before sunscreen",
    "Side Effects": "Mild tingling for sensitive skin",
    "Price": "₹699"
}

# Fictional Product B for comparison (normalized keys)
product_b = {
    "product_name": "Fictional Serum B",
    "concentration": "12% Vitamin C",
    "skin_type": ["Normal", "Dry"],
    "key_ingredients": ["Vitamin C", "Niacinamide"],
    "benefits": ["Brightening", "Reduces fine lines"],
    "how_to_use": "Apply 2 drops before moisturizer",
    "side_effects": "None reported",
    "price": "₹799"
}

if __name__ == "__main__":
    # STEP 1 + 2: Parse product data & generate questions
    parsed_product = run_pipeline(product_data)

    print("\n--- TEST ALL LOGIC BLOCKS ---\n")
    print(generate_benefits_block(parsed_product))
    print(generate_usage_block(parsed_product))
    print(generate_safety_block(parsed_product))
    print(generate_price_block(parsed_product))
    print(generate_ingredients_block(parsed_product))

    # STEP 3: Comparison block test
    comparison = compare_products(parsed_product, product_b)
    print("\n--- Comparison Block Output ---")
    print(comparison)

    # -------------------------------
    # PHASE 3: Template Engine & JSON
    # -------------------------------
    os.makedirs("outputs", exist_ok=True)
    template_agent = TemplateEngineAgent()

    # Generate Product Page
    product_page = template_agent.generate_product_page(parsed_product)
    template_agent.save_json(product_page, "product_page.json")
    print("\n✅ Product Page JSON created: outputs/product_page.json")

    # Generate Comparison Page
    comparison_page = template_agent.generate_comparison_page(parsed_product, product_b)
    template_agent.save_json(comparison_page, "comparison_page.json")
    print("✅ Comparison Page JSON created: outputs/comparison_page.json")

    # Generate FAQ Page
    faq_questions = {
        "Informational": [
            'What is GlowBoost Vitamin C Serum?', 
            'What does Vitamin C do for skin?', 
            'Who should use this serum?', 
            'Is this suitable for oily skin?'
        ],
        "Usage": [
            'How do I apply GlowBoost serum?', 
            'Should I use this before or after moisturizer?', 
            'Can I use this daily?', 
            'How many drops should I apply?'
        ],
        "Safety": [
            'Is tingling normal?', 
            'Can sensitive skin users apply this?', 
            'Are there side effects?', 
            'Can this cause breakouts?'
        ],
        "Purchase": [
            'What is the price?', 
            'Where can I buy GlowBoost?'
        ]
    }
    faq_page = template_agent.generate_faq_page(faq_questions)
    template_agent.save_json(faq_page, "faq.json")
    print("✅ FAQ Page JSON created: outputs/faq.json")
