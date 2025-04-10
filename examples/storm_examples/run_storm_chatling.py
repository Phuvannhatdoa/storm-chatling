import os
from dotenv import load_dotenv
from knowledge_storm.chatling_model import ChatlingAIModel
from knowledge_storm.engine import StormEngine
from knowledge_storm.rm import WikipediaRM

# Load .env file if present
load_dotenv()

# Khởi tạo ChatlingAIModel với thông tin từ môi trường hoặc thay trực tiếp API key
llm = ChatlingAIModel(
    api_key=os.getenv("CHATLING_API_KEY") or "YOUR_CHATLING_API_KEY",
    chatbot_id=os.getenv("CHATLING_CHATBOT_ID") or "YOUR_CHATBOT_ID"
)

# Retrieval module - dùng Wikipedia như ví dụ
rm = WikipediaRM()

# Khởi động STORM
storm = StormEngine(llm=llm, rm=rm)

# Thử nghiệm hỏi
query = "Ai là người sáng lập Phật giáo?"
result = storm.answer(query)

print("Câu trả lời từ ChatlingAI:")
print(result)
