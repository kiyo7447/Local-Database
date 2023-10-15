# HBaseとは
Apache HBaseは、Apache Hadoopプロジェクトの一部であり、分散型のNoSQLデータベースです。HBaseは、大量の構造化データを保存するために設計されており、GoogleのBigtableに基づいています。HBaseは、水平方向にスケーリングできるため、非常に大規模なデータセットを処理することができます。また、Hadoopエコシステムの一部であるため、MapReduceジョブとの統合が容易であり、データ処理のための高度な機能を提供します。HBaseは、Javaで書かれており、オープンソースで利用可能です。

# 参考 
* 公式サイト
HBaseは、、分散型のスケーラブルなビッグ データ ストア
https://hbase.apache.org/

# ポート番号
|Port Number|Protocol|Service Name|
|:---|:---|:---|
|8091|TCP|CouchBase Web Administration|
|8092|TCP|CouchBase API|

# メモ
Windowsに入れるのは、手間です。Linuxに入れるのが、簡単です。そして、Docker Composeが最も簡単です。


# 実行方法（Docker Compose）
```bash
コマンドからの使用について
# 起動
docker-compose -f .\docker-compose-standalone.yml up -d

# hbaseが起動しているか確認
docker ps

docker exec -it hbase hbase shell
# または
docker-compose -f .\docker-compose-standalone.yml exec hbase hbase shell

# hbase shellの使い方
create 'sns', 'blog'
put 'sns', 'user1', 'blog:post1', 'Hello World'
put 'sns', 'user1', 'blog:bitcoin', 'blog1'
scan 'sns'
# update
put 'sns', 'user1', 'blog:bitcoin', 'blog2'
scan 'sns'
put 'sns', 'user2', 'blog:bitcoin', 'blog3'

get 'sns', 'user1'
get 'sns', 'user2'

# 特定の列を持っているもの
scan 'sns', {COLUMN => 'blog:bitcoin'}

# 特定の件数分を習得
scan 'sns', {LIMIT => 2}

# blog:bitcoinの値がblog2のものを習得
scan 'sns', {FILTER => "ValueFilter(=, 'binary:blog2')"}

# 無効にして
disable 'sns'
# 有効時は、enable 'sns'で有効にする
# 削除
drop 'sns'
```
* master-status
http://localhost:16010/master-status

# Software Attributes
2023/10/15セットアップした場合のHBaseのバージョン情報は以下の通りです。
|Attribute Name|Value|Description|
|:---|:---|:---|
|HBase Version|1.2.6, revision=Unknown|HBase version and revision|
|HBase Compiled|Mon May 29 02:25:32 CDT 2017, busbey|When HBase version was compiled and by whom|
|HBase Source Checksum|7e8ce83a648e252758e9dae1fbe779c9|HBase source MD5 checksum|
|Hadoop Version|2.5.1, revision=2e18d179e4a8065b6a9f29cf2de9451891265cce|Hadoop version and revision|
|Hadoop Compiled|2014-09-05T23:05Z, kasha|When Hadoop version was compiled and by whom|
|Hadoop Source Checksum|6424fcab95bfff8337780a181ad7c78|Hadoop source MD5 checksum|
|ZooKeeper Client Version|3.4.6, revision=1569965|ZooKeeper client version and revision|
|ZooKeeper Client Compiled|02/20/2014 09:09 GMT|When ZooKeeper client version was compiled|
|Zookeeper Quorum|hbase:2181|Addresses of all registered ZK servers. For more, see zk dump.|
|Zookeeper Base Path|/hbase|Root node of this cluster in ZK.|
|HBase Root Directory|file:/tmp/hbase-root/hbase|Location of HBase home directory|
|HMaster Start Time|Sun Oct 15 00:53:40 UTC 2023|Date stamp of when this HMaster was started|
|HMaster Active Time|Sun Oct 15 00:53:42 UTC 2023|Date stamp of when this HMaster became active|
|HBase Cluster ID|70218a58-f056-4208-85c1-33a7da65fb64|Unique identifier generated for each HBase cluster|
|Load average|3.00|Average number of regions per regionserver. Naive computation.|
|Coprocessors|[]|Coprocessors currently loaded by the master|
|LoadBalancer|org.apache.hadoop.hbase.master.balancer.StochasticLoadBalancer|LoadBalancer to be used in the Master|

# GitHubリポジトリからのDocker Compose起動
https://github.com/big-data-europe/docker-hbase



# あとで、削除するメモ
Apache HBaseをDockerとDocker Composeを使ってセットアップする方法については、以下の手順を参照できます。なお、ここで紹介する方法はHBaseをスタンドアローンモードで実行するものとなっています。

1. **リポジトリのクローン**:
   最初に、GitHubから特定のリポジトリをクローンします。
   ```bash
   git clone https://github.com/big-data-europe/docker-hbase.git
   cd docker-hbase
   ```

2. **ファイアウォールの設定** (必要に応じて):
   ```bash
   sudo firewall-cmd --add-port=8088/tcp --zone=public --permanent
   sudo firewall-cmd --reload
   ```

3. **Docker Composeの実行**:
   ```bash
   docker-compose -f docker-compose-standalone.yml up -d
   ```
   上記のコマンドを実行することで、HBaseを含む各サービスが起動します【11†(source)】。

また、Apache HBaseのDocker Imageを利用して、ローカル環境でhbase-shellを実行する方法もありますが、これはスタンドアローンモードで実行する方法となっています【7†(source)】。

これらの手順を参考に、Apache HBaseをDockerとDocker Composeを使ってセットアップしてみてください。


# 参考文献
Apache HBaseをDocker Composeで動かすためのいくつかのGitHubリポジトリがあります。以下に、それぞれのリポジトリの特徴とリンクを示します。

1. **[HBigdata/docker-compose-hbase](https://github.com/HBigdata/docker-compose-hbase)リポジトリ**:
   - DockerとDocker Composeのデプロイメント、ネットワークの作成、ZookeeperとHadoopの環境のインストール、JDKとHBaseのダウンロード、設定、起動スクリプト、およびイメージの構築に関する指示が含まれています【39†(source)】。

2. **[tsuyo/apache-hbase-docker](https://github.com/tsuyo/apache-hbase-docker)リポジトリ**:
   - シングルノードクラスター用のApache HBase Dockerfileが提供されています。このリポジトリでは、特定のHBaseバージョンのイメージをビルドして実行するための指示が含まれています【40†(source)】。

3. **[dajobe/hbase-docker](https://github.com/dajobe/hbase-docker)リポジトリ**:
   - この構成では、埋め込みZookeeperを含むHBaseを実行するDockerコンテナをビルドします。ただし、このアプローチは、コンテナのホスト名のエントリを追加するためにローカルサーバーの `/etc/hosts` ファイルを編集することが必要です【41†(source)】。

4. **[smizy/docker-hbase](https://github.com/smizy/docker-hbase)リポジトリ**:
   - AlpineベースのApache HBase Dockerイメージが提供されており、セットアップは小さく保たれています【42†(source)】。

これらのリポジトリは、Apache HBaseをDocker Composeで動かすための異なるアプローチを提供しています。