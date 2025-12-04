# rpi-clock-github

このリポジトリは Raspberry Pi 向けのシンプルな時計アプリケーションの雛形です。Python ベースで、CI とテストを含みます。

使い方の例:

- ローカルで開発する場合:
  # rpi-clock

  Raspberry Pi 向けのシンプルな時計アプリケーションの雛形です。Python で書かれており、テスト（pytest）と GitHub Actions CI を含みます。

  ## 目的

  このリポジトリは小さなデモ用ライブラリ／アプリケーションの雛形を提供します。ローカルでの開発、テスト、自動テスト（CI）までのワークフローを含みます。

  ## 使い方（ローカル）

  ```bash
  cd /DATA/rpi-clock
  python3 -m venv .venv
  source .venv/bin/activate
  python -m pip install --upgrade pip
  python -m pip install -r requirements.txt
  # テスト実行
  PYTHONPATH=src pytest -q
  # 実行例（時計を表示）
  python -m rpi_clock.clock
  ```

  注: ソースは `src/rpi_clock` にあり、テストは `tests/` にあります。テスト実行時は `PYTHONPATH=src` を指定するか、仮想環境にパッケージをインストールしてください。

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
