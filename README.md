# ローカル処理のデータベース
### [ObjectBox](./ObjectBox/) 
- **タイプ**: オブジェクト指向データベース
- **特徴**:
    - モバイルデバイスとエッジコンピューティング向けに設計されています。
    - 高速で、低レイテンシーでのデータアクセスと効率的なデータストレージを提供します。
### [Realm](./Realm/)
- **タイプ**: オブジェクト指向データベース
- **特徴**:
   - モバイルアプリケーション向けに設計され、オブジェクトを直接保存できることを特徴としています
   - Realmは、データベースとアプリケーションのオブジェクト間でシームレスなマッピングを提供し、データアクセスと操作を容易にします。
### [SQLite](./SQLite/)
- **タイプ**: リレーショナルデータベース
- **特徴**:
   - 軽量で、設定が不要で、サーバーレスで、セルフコンテインド（外部依存がない）なデータベースエンジンです。
   - トランザクション性をサポートし、標準のSQLクエリ言語を使用します。
   - モバイルデバイス、埋め込みシステム、そしてデスクトップアプリケーションで広く利用されています。

### [memcached](./memcached/)
- **タイプ**: インメモリキーアバリューストア
- **特徴**:
   - 高速なデータアクセスを提供するために、データをメモリ内にキャッシュすることを目的としています。
   - シンプルなキー値ストアであり、データベースやAPI呼び出しの結果をキャッシュして、後続の同じクエリのレスポンスタイムを大幅に削減できます。
## Now
### [MongoDB](./MongoDB/)
- **タイプ**: ドキュメント指向データベース
- **特徴**:
    - JSON-like（BSON）ドキュメントを用いてデータを保存し、構造化、半構造化、および多構造化データを効率的に管理できます。
    - スキーマレスであり、データモデルが柔軟であるため、開発が迅速であり、変更が容易です。
    - 高いパフォーマンス、スケーラビリティ、および使いやすさを提供し、ウェブアプリケーション、モバイルアプリケーション、リアルタイムアナリティクスなど、多くの異なる用途に適しています。
### [neo4j](./neo4j/)
- **タイプ**: グラフデータベース
- **特徴**:
    - エンティティ間の関係を表現しやすいグラフデータモデルを採用しています。
    - グラフの探索やパターンマッチングのクエリを効率的に実行できる特別なクエリ言語、Cypherを提供しています。
    - 社会ネットワーク、推薦システム、知識グラフなど、関係性が重要なドメインでの利用に適しています。
### [Apache HBase](./ApacheHBase/)
* ***タイプ***: 分散型NoSQLデータベース
* ***特徴***:
  * Google BigTableのオープンソース実装であり、カラム指向のデータモデルを採用しています。
  * Hadoopエコシステムと統合されており、大量のデータを効率的に処理できるように設計されています。
  * リアルタイムの読み書きアクセスが可能であり、大量のデータを効率的に格納および管理できます。
### [Cassandra](./Cassandra/)
* ***タイプ***: 分散型NoSQLデータベース
* ***特徴***:
  * カラム指向であり、BigTableのデータモデルとAmazon Dynamoのフルトレラントなデザインの特徴を組み合わせて設計されています。
  * 高い書き込みと読み込みのパフォーマンス、および優れたスケーラビリティと可用性を提供します。
  * データは分散され、冗長化され、複数のノードにレプリケートされるため、障害の耐性があります。


## TODO
* [Couchbase Lite](./CouchbaseLite/)
* [Firebase](./Firebase/)
* [InfluxDB](./InfluxDB/)
* [LevelDB](./LevelDB/)
* [TinyDB](./TinyDB/)
* [Berkeley DB](./BerkeleyDB/)
* [RocksDB](./RocksDB/)
* [PouchDB](./PouchDB/)
* [CouchDB](./CouchDB/)
* [Apache IoTDB](./ApacheIoTDB/)
* [Apache Cassandra](./ApacheCassandra/)
* [Apache Hive](./ApacheHive/)
* [Apache Phoenix](./ApachePhoenix/)
* [Apache Ignite](./ApacheIgnite/)
* [Apache Druid](./ApacheDruid/)
* [Apache Pinot](./ApachePinot/)
* [Apache Kudu](./ApacheKudu/)
* [Apache Tajo](./ApacheTajo/)
* [Apache Kylin](./ApacheKylin/)
* [Apache Flink](./ApacheFlink/)
* [Apache Spark](./ApacheSpark/)
* [Apache Kafka](./ApacheKafka/)
* [Apache NiFi](./ApacheNiFi/)
* [Apache Nutch](./ApacheNutch/)
* [Apache Solr](./ApacheSolr/)
* [Apache Lucene](./ApacheLucene/)
* [Apache Hadoop](./ApacheHadoop/)
* [Apache ZooKeeper](./ApacheZooKeeper/)
## TODO
* 
ローカルで使用できるモバイルやIoT向けのデータベースにはいくつかのオプションがあります。
1. **SQLite**：非常に軽量で、多くのモバイルアプリで一般的に使用されています。アンドロイドやiOS、さらには多くのIoTデバイスでも利用可能です。
2. **Realm**：モバイルオプティマイズされたデータベースであり、高いパフォーマンスと使い易さが売りです。iOSとAndroidの両方で使用できます。
3. **Firebase Realtime Database / Firestore**：リアルタイムのデータ同期が必要な場合に便利ですが、オフラインでもローカルにデータを保存できます。
4. **Couchbase Lite**：JSON形式でデータを保存し、モバイルデバイスとクラウド間での同期もサポートしています。
5. **RocksDB**：Facebookによって開発された埋め込み型のキー・バリューストアです。IoTデバイスでよく使用されます。
6. **Berkeley DB**：埋め込み型のデータベースで、キー・バリュー、列、文書など複数のデータモデルをサポートしています。
7. **PouchDB / CouchDB**：PouchDBはブラウザでも動作するJavaScriptデータベースで、CouchDBとの同期が可能です。IoTデバイスでの利用もあります。
8. **InfluxDB**：時系列データに特化したデータベースで、IoTセンサーデータなどによく使用されます。
9. **LevelDB**：Googleによって開発された高速なキー・バリューストアで、特に読み取りと範囲クエリが高速です。
10. **TinyDB**: Pythonで動作する小型のデータベースで、IoTデバイスでの小規模なデータ保存に使用されます。
各データベースはそれぞれ特有の特性と制限があります。

# 参考文献
* [IoT アプリケーション市場でトップのデータベース](https://www.intuz.com/guide-on-top-iot-databases)
* [2003 モバイルデータベース iOS/Andorid SQLiteの代替案](https://greenrobot.org/news/mobile-databases-sqlite-alternatives-and-nosql-for-android-and-ios/)
### Apacheシステム構成
* [モノのインターネット用データベース](https://iotdb.apache.org/)

