https://memcached.org/
# memcahedを使う

```bash
# memcachedのインストール
sudo apt install memcached
# memcachedの起動
sudo systemctl start memcached
# memcachedの起動確認
sudo systemctl status memcached
# memcachedの停止
sudo systemctl stop memcached
# memcachedの自動起動設定
sudo systemctl enable memcached
# memcachedの自動起動設定解除
sudo systemctl disable memcached
# memcachedの設定ファイル
/etc/memcached.conf
```
# memcachedの使い方
## Dockerfileでの使い方
```bash
docker build -t memcached-image .

docker run --rm -d -p 11211:11211 --name memcached-container memcached-image

```
# # Docker Composeでの使い方
```bash
docker-compose up -d
```