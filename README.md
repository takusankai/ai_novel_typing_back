# ai_novel_typing

技育CAMP マンスリーハッカソン Vol.13 2024/1/12～2024/1/21

このリポジトリは「まるねこアイスクリーム開発譚」チームの開発作品のバックエンド部分です。

フロントエンド部分のURL：https://github.com/takusankai/ai_novel_typing_flont

## やっていること

openaiモジュールを使って、chatGPTのAPIにアクセスしてシナリオ文章を生成。

対応する選択肢文章を2種類生成。

pykakashiで選択肢のローマ字バージョンを生成。

flaskを利用したAPIアプリケーションとして、生成結果のjson形式でフロントに返却。
