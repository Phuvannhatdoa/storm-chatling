import requests

class ChatlingAIModel:
    def __init__(self, slug):
        self.slug = slug
        self.api_url = f"https://chatling.ai/api/embed/{slug}"

    def invoke_message(self, prompt):
        try:
            res = requests.post(
                self.api_url,
                json={"message": prompt}
            )
            res.raise_for_status()
            data = res.json()
            return data.get("text", "[Không có nội dung phản hồi]")
        except Exception as e:
            return f"[❌] Lỗi khi gọi ChatlingAI: {e}"
