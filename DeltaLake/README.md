
'''powershell
docker build -t delta-lake-image .

# 起動
docker run -it --name delta-lake delta-lake-image
# ポートを開けて起動
docker run -it --name delta-lake -p 7077:7077 -p 8080:8080 delta-lake-image

# 起動しているコンテナに入る
docker exec -it delta-lake /bin/bash

spark-shell --packages io.delta:delta-core_2.12:0.8.0


```
## Docker Hub
https://hub.docker.com/r/deltaio/delta-docker

```

docker pull deltaio/delta-docker -t delta-lake-image
docker scout quickview deltaio/delta-docker

```
## GitHub
https://github.com/delta-io/delta-docs/tree/main/static/quickstart_docker
```


```


# ストレージとSparkの選定（AWS編）
AWS上でDelta Lakeを設定する方法はいくつかあります。以下に、異なる方法とそれぞれの基本的な手順を示します。
Delta Formatという規格を使うことで、データのバージョン管理や、データの変更をトランザクションで管理することができる。
Delta Lakeというのは、Delta Formatを使うためのライブラリのこと。

1. **AWS Glueを使用する**:
   - AWS GlueでDelta Lakeを有効にするには、`--datalake-formats`ジョブパラメータに`delta`を指定し、`--conf`というキーをAWS Glueジョブに作成します【27†(source)】。
   https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-delta-lake.html
   - ストレージは、S3だが、Sparkエンジンは、Glueが提供するものを使う。

2. **AWS EMRを使用する**:
   - Delta Lake用のEMRを設定するには、各クラスタノードに外部ライブラリをインストールするためのブートストラップアクションを使用できます【28†(source)】。
   - Apache Hadoop、Apache Spark、HBaseなどのオープンソースフレームワークをサポートしているため。
   - 大量のデータを効率的に処理および分析することができます

3. **Databricksを使用する**:
   - AWSアカウントにDatabricksアカウントを設定し、バッチおよびストリーミングデータのデータ摂取ソースおよびストレージを設定します【29†(source)】。
   - DatabricksプラットフォームはApache Sparkの最適化に重点を置いているため。
   - データの探索、クレンジング、分析、および機械学習のための統合された環境を提供します。
   - オンプレ非対応、Delta Lakeのサポートは、Databricksのみ。

4. **EC2とApache Sparkを使用する**:
   - AWSのEC2上でApache SparkとDelta Lakeを設定する方法については、ステップバイステップのチュートリアルが利用可能です【30†(source)】。
   - ガリガリ用意するオンプレミスもイケる。DockerやDocker Composeでも用意できる。



5. **Amazon EMRを使用する**:
   - Amazon EMRのリリース6.9.0以降では、Apache Spark 3.xを使用してAmazon EMRクラスター上でDelta Lakeテーブルを使用できます【31†(source)】。

これらの方法のいずれかを選んで、AWS上でDelta Lakeを設定できます。それぞれの方法には異なる前提条件や設定が必要であるため、プロジェクトの要件に基づいて最適な方法を選択することが重要です。また、これらの方法の詳細については、関連するドキュメントやリソースを参照することをお勧めします。
