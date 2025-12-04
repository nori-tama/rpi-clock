# rpi-clock-github

このリポジトリは Raspberry Pi 向けのシンプルな時計アプリケーションの雛形です。Python ベースで、CI とテストを含みます。

使い方の例:

- ローカルで開発する場合:
  ```bash
  cd rpi-clock-github
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  python -m src.rpi_clock.clock
  ```

- GitHub に公開する場合（`gh` CLI がある場合）:
  ```bash
  cd rpi-clock-github
  gh repo create <OWNER>/rpi-clock-github --public --source=. --push
  ```

ご希望があれば、リポジトリ名やライセンスを変更して GitHub に作成します。
