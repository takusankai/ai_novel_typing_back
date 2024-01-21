from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import os
from openai import OpenAI
import json
from pykakasi import kakasi

kakasi = kakasi()
# 漢字⇒ヘボン式アルファベット変換を設定
kakasi.setMode("J", "a")
# カタカナ⇒ヘボン式アルファベット変換を設定
kakasi.setMode("K", "a")
# ひらがな⇒ヘボン式アルファベット変換を設定
kakasi.setMode("H", "a")
conv = kakasi.getConverter()

# デバッグ用
# text = "じゃあちゃんと注意しゅるふぉ"
# print(conv.do(text))

# Flaskの起動
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False
CORS(app)

# ルーティングの設定
@app.route('/',methods=['GET','POST'])

def home():
    return generate()

def generate():

    data = request.get_json()

    # デバッグ用
    # print(data)
    # print(data.get('key'))
    
    # APIクライアントの初期化
    client = OpenAI(

        # This is the default and can be omitted
        organization=os.environ.get('OpenAI_organization'),
        api_key=os.environ.get('API_KEY_openai')

    )

    #messages = data.get('messages', [])

    # メッセージの設定
    messages = [
        {"role": "assistant", "content": "前回のシナリオは「" + data.get('key') + "」でした。この続きのシナリオを書いてください。形式としてシナリオ名及びシナリオ内容と、それに対応する2つの行動の選択肢を出力してください。jsonフォーマット { シナリオ名:文章, シナリオ内容:文章, 選択肢1:文章,選択肢2:文章:} の形で返してください。"},
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

    # 生成されたテキストが複数だった時の取得
    # ながーい1プロンプトで処理するならforループは不要
    # for i, choice in enumerate(response.choices):
        # print(f"\nresult {i}:")
        # print(choice.message.content.strip())
    choice = response.choices[0]

    # json.loads関数を使ってPythonデータ構造のJSON形式への変換
    json_data = json.loads(choice.message.content.strip())
    
    # デバッグ用
    print(json_data['選択肢1'])
    print(json_data['選択肢2'])

    # kakashiで選択肢を日本語をヘボン式アルファベットに変換したものを新たに追加
    pick1_conv = conv.do(json_data['選択肢1'])
    pick2_conv = conv.do(json_data['選択肢2'])

    # デバッグ用
    print(pick1_conv)
    print(pick2_conv)

    # json_dataに追加
    json_data['選択肢1のローマ字'] = pick1_conv
    json_data['選択肢2のローマ字'] = pick2_conv

    # デバッグ用
    print(json_data)

    # json_dataをpythonの文字列型に変換
    json_data_str = json.dumps(json_data, ensure_ascii=False)

    # ながーい1プロンプトで処理するならforループは不要
    # return jsonify([choice.message.content for choice in response.choices])
    # return jsonify(choice.message.content.strip())

    return jsonify(json_data_str)

# 初回の起動処理
if __name__ == '__main__':
    app.run(debug=True)
