# knowledge_storm/engine.py

class StormEngine:
    def __init__(self, llm, rm):
        self.llm = llm
        self.rm = rm

    def answer(self, query: str) -> str:
        context = self.rm.retrieve(query)
        prompt = f"{context}\n\nCâu hỏi: {query}"
        return self.llm.generate(prompt)
