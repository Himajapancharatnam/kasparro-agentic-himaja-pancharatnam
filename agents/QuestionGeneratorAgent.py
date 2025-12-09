class QuestionGeneratorAgent:
    """
    Agent 2: Generates categorized user questions based on product data.
    """

    def run(self, product: dict) -> dict:

        return {
            "Informational": [
                "What is GlowBoost Vitamin C Serum?",
                "What does Vitamin C do for skin?",
                "Who should use this serum?",
                "Is this suitable for oily skin?"
            ],
            "Usage": [
                "How do I apply GlowBoost serum?",
                "Should I use this before or after moisturizer?",
                "Can I use this daily?",
                "How many drops should I apply?"
            ],
            "Safety": [
                "Is tingling normal?",
                "Can sensitive skin users apply this?",
                "Are there side effects?",
                "Can this cause breakouts?"
            ],
            "Purchase": [
                "What is the price?",
                "Where can I buy GlowBoost?"
            ]
        }
