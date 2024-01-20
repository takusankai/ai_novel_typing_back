from flask import Flask, request, jsonify, make_response
import os
from openai import OpenAI
import json

# Flaskの起動
app = Flask(__name__)

#@app.route('/generate', methods=['POST'])
@app.route('/')
def home():
    return generate()

def generate():
    #data = request.get_json()
    # APIクライアントの初期化
    client = OpenAI(
        # This is the default and can be omitted
        organization=os.environ.get('OpenAI_organization'),
        api_key=os.environ.get('API_KEY_openai')
    )

    #messages = data.get('messages', [])

    # メッセージの設定
    messages = [
        {"role": "system", "content": "海で冒険をするシナリオのノベルゲームを作ってください。シナリオと２つの選択肢を考えてください。ここではシナリオを書いてください。"},
        {"role": "assistant", "content": "選択肢１の文章を書いて。"},
        {"role": "assistant", "content": "選択肢２の文章を書いて。"}
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
    print(response)
    for i, choice in enumerate(response.choices):
        print(f"\nresult {i}:")
        print(choice.message.content.strip())
    #修正前
    #return jsonify([choice['message']['content'] for choice in response['choices']])
    #修正後(rawjson)
    #return jsonify([choice.message.content for choice in response.choices])
        
    #日本語出力
     # 生成されたテキストの取得
    result = [choice.message.content for choice in response.choices]
     # 結果をJSONファイルとして出力
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    # JSON形式での返却（日本語をそのまま出力）
    return make_response(json.dumps(result, ensure_ascii=False))

if __name__ == '__main__':
    app.run(debug=True)