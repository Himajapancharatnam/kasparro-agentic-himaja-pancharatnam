class DataParserAgent:
    """
    Agent 1: Parses the raw product data and converts it into
    a clean internal model (Python dictionary).
    """

    def run(self, raw_data: dict) -> dict:
        if not isinstance(raw_data, dict):
            raise ValueError("Input must be a dictionary.")

        return {key.replace(" ", "_").lower(): value for key, value in raw_data.items()}
