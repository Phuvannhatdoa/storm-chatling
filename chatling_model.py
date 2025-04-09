# knowledge_storm/chatling_model.py

import requests
from .base import LanguageModel  # nếu không có, import từ đúng base class bạn thấy trong `lm.py`

class ChatlingAIModel(LanguageModel):
    def __init__(self, api_key: str, chatbot_id: str):
        self.api_key = api_key
        self.chatbot_id = chatbot_id

    def complete(self, messages, **kwargs) -> str:
        url = f"https://app.chatling.ai/api/v1/chatbots/{self.chatbot_id}/chat"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        prompt = messages[-1]["content"]  # dùng nội dung tin nhắn cuối cùng

        body = {
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()
        return data.get("message", "Không có phản hồi từ Chatling")
