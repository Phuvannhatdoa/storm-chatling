# knowledge_storm/base.py

class LanguageModel:
    def generate(self, prompt: str) -> str:
        raise NotImplementedError("You need to implement the generate method.")
