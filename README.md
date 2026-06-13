# file-outputer

Dify のワークフローから、Base64 エンコード済みのバイナリデータをファイルとして出力するためのツールプラグインです。

## 概要

`file-outputer` は、LLM やワークフロー内で生成した Base64 データを受け取り、Dify の Blob メッセージとして返します。PDF、Excel、ZIP、画像など、任意のバイナリファイルをワークフローの出力として扱いたい場合に利用できます。

## プラグイン情報

- 作者: `mikoto2000`
- バージョン: `0.0.1`
- 種別: Dify tool plugin
- ランナー: Python 3.12
- 最小 Dify バージョン: `1.14.0`
- 対応アーキテクチャ: `amd64`, `arm64`

## ツール

### file-outputer

Base64 エンコード済みデータをデコードし、指定されたファイル名と MIME type を付けて Blob として返します。

#### 入力パラメータ

| パラメータ | 必須 | 説明 |
| --- | --- | --- |
| `content_base64` | はい | Base64 エンコードされたバイナリ内容です。 |
| `output_filename` | はい | 出力ファイル名です。例: `result.xlsx`, `result.pdf`, `result.zip` |
| `mime_type` | いいえ | 出力ファイルの MIME type です。未指定の場合は `application/octet-stream` として扱います。 |

#### 出力

デコードしたバイナリデータを Blob メッセージとして返します。メタデータには以下が含まれます。

- `filename`: 出力ファイル名
- `mime_type`: 出力ファイルの MIME type

## Data URI 形式

実装では、以下のような Data URI 形式の Base64 文字列にも対応しています。

```text
data:application/pdf;base64,JVBERi0xLjQK...
```

Data URI に MIME type が含まれている場合は、その MIME type が出力メタデータに反映されます。

## 利用例

PDF ファイルを出力する場合の入力例です。

```json
{
  "content_base64": "JVBERi0xLjQK...",
  "output_filename": "result.pdf",
  "mime_type": "application/pdf"
}
```

Excel ファイルを出力する場合の入力例です。

```json
{
  "content_base64": "UEsDBBQAAAAI...",
  "output_filename": "result.xlsx",
  "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
}
```

## 開発

依存関係をインストールします。

```bash
pip install -r requirements.txt
```

プラグインをローカルで起動します。

```bash
python main.py
```

## ファイル構成

```text
.
├── main.py
├── manifest.yaml
├── provider/
│   ├── file-outputer.py
│   └── file-outputer.yaml
├── requirements.txt
└── tools/
    ├── file-outputer.py
    └── file-outputer.yaml
```

## 注意事項

- Base64 として不正な文字列が渡された場合、エラーメッセージをテキストで返します。

## ライセンス

このプロジェクトは MIT ライセンスで公開されています。詳細は [LICENSE](LICENSE) を参照してください。

