##
### 公式ドキュメント
https://docs.objectbox.io/
### ソース  
https://github.com/objectbox/objectbox-examples/tree/main/java-main-maven
## 必要なもの
VS Code で Java を使用するには、次のものが必要です。
* Java Extension Pack: Java の開発に必要な基本的な拡張機能をバンドルしたパッケージです。
* Maven for Java: Maven プロジェクトのサポートを提供します。
* Gradle for Java: Gradle プロジェクトのサポートを提供します。
## プロジェクトの作成
```
# プロジェクトの作成
mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

# mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=access-objectbox -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

cd my-app
# ビルド
mvn compile
# 実行
mvn exec:java
```
# エラーについて
## pom.xmlの作成
適宜エラーの内容に合わえて修正する必要がある。
Gitのソースがなければエラーは解決できなかった。

# TODO
mdbファイルを見るツールを調べて扱ってみる。
