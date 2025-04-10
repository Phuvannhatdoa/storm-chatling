from knowledge_storm.chatling_model import ChatlingAIModel

model = ChatlingAIModel(slug="5k6HgsSSo3DXblV")
response = model.invoke_message("Xin chào, bạn tên là gì?")
print("💬 ChatlingAI trả lời:\n", response)
