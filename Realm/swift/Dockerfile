# 基本イメージとして公式のSwiftイメージを使用
FROM swift:5.4-slim

# 必要なツールをインストール
RUN apt-get update && apt-get install -y \
    ruby \
    ruby-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# CocoaPodsをインストール
RUN gem install cocoapods

# プロジェクトディレクトリをコピー
# この例では、プロジェクトディレクトリは`/app`にコピーされます
# ご自身のプロジェクトのディレクトリ構造に応じて変更してください
COPY . /app

# プロジェクトディレクトリに移動
WORKDIR /app

# Podfileがプロジェクトディレクトリに存在することを確認し、依存関係をインストール
RUN pod install

# プロジェクトをビルド
RUN swift build

# プロジェクトを実行
CMD ["swift", "run"]
