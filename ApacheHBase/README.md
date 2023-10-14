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

# コマンドからの使用について
```
# hbaseが起動しているか確認
docker ps

docker exec -it hbase hbase shell
# または
docker-compose exec hbase hbase shell

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
# 削除
drop 'sns'
```

```

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