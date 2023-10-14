# 基本イメージとしてApache Sparkのイメージを使用
FROM bitnami/spark:3

# Delta Lakeのバージョンを設定
ARG DELTA_LAKE_VERSION=0.8.0

# Delta Lakeのjarファイルをダウンロード
RUN curl -L -o /opt/bitnami/spark/jars/delta-core_${DELTA_LAKE_VERSION}.jar https://repo1.maven.org/maven2/io/delta/delta-core_2.12/${DELTA_LAKE_VERSION}/delta-core_2.12-${DELTA_LAKE_VERSION}.jar

# Delta Lakeのjarを含むSparkのクラスパスを設定
ENV SPARK_CLASSPATH="/opt/bitnami/spark/jars/delta-core_${DELTA_LAKE_VERSION}.jar"
