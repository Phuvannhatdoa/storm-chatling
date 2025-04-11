#!/bin/bash

echo "🚀 Đang setup STORM CLI với Groq (Mistral-7B)..."

# Bước 1: Clone bản gốc từ Stanford
cd ~
git clone https://github.com/stanford-oval/storm.git storm_groq
cd storm_groq

# Bước 2: Tạo môi trường ảo
python3 -m venv .venv
source .venv/bin/activate

# Bước 3: Cài đặt STORM
pip install --upgrade pip
pip install .

# Bước 4: Tạo file cấu hình Groq + Mistral-7B (tiếng Việt)
mkdir -p ~/.storm

cat <<EOF > ~/.storm/config.yml
default:
  provider: groq
  model: mistral-7b
  temperature: 0.7
  top_p: 1.0
  max_tokens: 1024
  api_key: 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
EOF

cat <<EOF > ~/.storm/profile.yml
name: "Trợ lý tiếng Việt"
description: "Trợ lý AI sử dụng Mistral-7B trả lời tiếng Việt chuẩn xác và rõ ràng."
persona: |
  Bạn là một trợ lý AI thông minh, trả lời bằng tiếng Việt. Giải thích rõ ràng, dễ hiểu. Luôn trả lời bằng tiếng Việt, kể cả khi người dùng hỏi bằng ngôn ngữ khác.
EOF

# Bước 5: Tạo alias `storm`
echo "alias storm='~/storm_groq/.venv/bin/storm'" >> ~/.bashrc
source ~/.bashrc

echo "✅ Đã setup xong! Bạn có thể test lệnh sau:"
echo "storm run --input \"Tứ Diệu Đế là gì?\""
