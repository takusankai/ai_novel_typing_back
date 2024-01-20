
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    organization=os.environ.get('OpenAI_organization'),
    api_key=os.environ.get('API_KEY_openai')
)

# メッセージの設定
messages = [
    {"role": "assistant", "content": "海で冒険をするシナリオのノベルゲームを作ってください。選択肢を3つ提示してください。"},
    {"role": "assistant", "content": "前回提示した選択肢から一つを選んでください。その選択肢をもとに3つの選択肢を生成してください。選択肢の1文字目は違うローマ字にしてください。"}
]

# APIリクエストの設定

response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # GPTのエンジン名を指定します
    messages=messages,
    max_tokens=300,  # 生成するトークンの最大数
    n=1,  # 生成するレスポンスの数
    stop=None,  # 停止トークンの設定
    temperature=0.7,  # 生成時のランダム性の制御
    top_p=1,  # トークン選択時の確率閾値
)

# 生成されたテキストの取得
for i, choice in enumerate(response.choices):
    print(f"\nresult {i}:")
    print(choice.message.content.strip())