# rpi-clock-github

このリポジトリは Raspberry Pi 向けのシンプルな時計アプリケーションの雛形です。Python ベースで、CI とテストを含みます。

使い方の例:

# rpi-clock

Raspberry Pi 向けのシンプルな時計アプリケーションの雛形です。Python で書かれており、簡単な実行例を含みます。

## 使い方（ローカル）

```bash
cd /DATA/rpi-clock
# 任意: 仮想環境を使う場合
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
# 実行例（時計を表示）
python -m rpi_clock.clock
```

注: ソースは `src/rpi_clock` にあります。現在、このリポジトリには自動テスト（CI）は含まれていません。

## GitHub に公開する

リポジトリを GitHub に作成するには `gh` CLI を使うか、Web UI で新しいリポジトリを作成してください。`gh` を使う例:

```bash
cd /DATA/rpi-clock
gh repo create nori-tama/rpi-clock --public --source=. --remote=origin --push
```

SSH 鍵を使う場合はリモートを SSH URL に設定します:

```bash
git remote set-url origin git@github.com:nori-tama/rpi-clock.git
git push -u origin main
```

## ライセンス

このリポジトリは `LICENSE` ファイルに記載されたライセンスのもとで配布されます。

## 貢献

バグ報告やプルリクエストは歓迎します。まず Issue を立ててください。
