# ベースイメージとしてOpenJDKを使用
FROM openjdk:11-jdk

# 必要なツールをインストール
RUN apt-get update && apt-get install -y ruby ruby-dev build-essential curl unzip && rm -rf /var/lib/apt/lists/*

# Kotlinのバージョンを指定
ENV KOTLIN_VERSION=1.5.31

# Kotlinコンパイラをダウンロードし、インストール
RUN curl -L https://github.com/JetBrains/kotlin/releases/download/v${KOTLIN_VERSION}/kotlin-compiler-${KOTLIN_VERSION}.zip -o /tmp/kotlin-compiler.zip \
    && unzip /tmp/kotlin-compiler.zip -d /opt \
    && rm /tmp/kotlin-compiler.zip

# CocoaPodsのインストール
RUN gem install cocoapods

# Kotlinコンパイラのバイナリへのパスを設定
ENV PATH=$PATH:/opt/kotlinc/bin

# ソースコードをコンテナにコピー
COPY . /app
WORKDIR /app

# Realmをインストール
# RUN pod install realm
# ↓
# Podfileがある場合は、依存関係をインストール
# Podfileを作成し、Realmの依存関係を指定してください
RUN if [ -f Podfile ]; then pod install; fi


# ソースコードをコンパイル
# RUN kotlinc main.kt model.kt -include-runtime -d main.jar
# ↓
RUN kotlinc *.kt -include-runtime -d main.jar

# コマンドを設定（コンテナが起動したときに実行）
CMD ["java", "-jar", "main.jar"]
