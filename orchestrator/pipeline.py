from agents.DataParserAgent import DataParserAgent
from agents.QuestionGeneratorAgent import QuestionGeneratorAgent

def run_pipeline(raw_product_data):
    """
    Orchestrator pipeline:
    1. Parse raw data
    2. Generate questions
    Returns normalized product dictionary
    """
    print("STEP 1: Parsing Product Data...")
    parser = DataParserAgent()
    product = parser.run(raw_product_data)
    print("Parsed Product:")
    print(product)

    print("\nSTEP 2: Generating Questions...")
    question_agent = QuestionGeneratorAgent()
    questions = question_agent.run(product)
    print("Generated Questions:")
    print(questions)

    # Return parsed product for further logic blocks
    return product
