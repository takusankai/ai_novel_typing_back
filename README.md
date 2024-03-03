# GPT_API

## 概要
技育Camp マンスリーハッカソン vol.13にて作った「Typing Journy -Only Rode-」のバックエンド部分です。<br>
2024/1/12～2024/1/21

## やっていること
openaiモジュールを使って、GPTのAPIにアクセスしてシナリオ文章を生成。<br>
対応する選択肢文章を2種類生成。<br>
pykakashiで選択肢のローマ字バージョンを生成。<br>
flaskにて、これらの生成結果をjson形式でアクセス側に返却する。

## 必要なもの
.envファイルにOpenAIのAPIキーを入れる。
