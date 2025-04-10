from storm.llms.chatlingai import ChatlingAIModel

llm = ChatlingAIModel(
    api_key="zSQ4D2blNdg8upoNCz6dUmPdt2vCFGc7y8ULzJ7gb2PcfL4CPUbdtpvoU43elFgq",  # <-- Thay bằng API key Chatling của bạn
    chatbot_slug="5k6HgsSSo3DXblV"  # <-- Slug từ link chia sẻ
)

response = llm.invoke("Xin chào, bạn là ai?")
print("Câu trả lời từ ChatlingAI:")
print(response)

