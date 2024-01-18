import os
import openai

openai.api_key = 

# メッセージの設定
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "空の色を教えてください。"}
]

# APIリクエストの設定
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # GPTのエンジン名を指定します
    messages=messages,
    max_tokens=100,  # 生成するトークンの最大数
    n=5,  # 生成するレスポンスの数
    stop=None,  # 停止トークンの設定
    temperature=0.7,  # 生成時のランダム性の制御
    top_p=1,  # トークン選択時の確率閾値
)

# 生成されたテキストの取得
for i, choice in enumerate(response.choices):
    print(f"\nresult {i}:")
    print(choice.message['content'].strip())