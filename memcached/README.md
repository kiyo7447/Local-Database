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

docker run -d -p 11211:11211 --name memcached memcached-image

```
# # Docker Composeでの使い方
```bash
docker-compose up -d
```
# Pythonでの使い方
https://github.com/kiyo7447/Python-Logic/blob/main/Section12_Database/141memcache.py
## 接続情報
```bash
stats: [('127.0.0.1:11211 (1)', {'pid': '1', 'uptime': '7', 'time': '1697278361', 'version': '1.6.21', 'libevent': '2.1.12-stable', 'pointer_size': '64', 'rusage_user': '0.010846', 'rusage_system': '0.009526', 'max_connections': '1024', 'curr_connections': '2', 'total_connections': '3', 'rejected_connections': '0', 'connection_structures': '3', 'response_obj_oom': '0', 'response_obj_count': '1', 'response_obj_bytes': '16384', 'read_buf_count': '2', 'read_buf_bytes': '32768', 'read_buf_bytes_free': '0', 'read_buf_oom': '0', 'reserved_fds': '20', 'cmd_get': '0', 'cmd_set': '0', 'cmd_flush': '0', 'cmd_touch': '0', 'cmd_meta': '0', 'get_hits': '0', 'get_misses': '0', 'get_expired': '0', 'get_flushed': '0', 'delete_misses': '0', 'delete_hits': '0', 'incr_misses': '0', 'incr_hits': '0', 'decr_misses': '0', 'decr_hits': '0', 'cas_misses': '0', 'cas_hits': '0', 'cas_badval': '0', 'touch_hits': '0', 'touch_misses': '0', 'store_too_large': '0', 'store_no_memory': '0', 'auth_cmds': '0', 'auth_errors': '0', 'bytes_read': '7', 'bytes_written': '0', 'limit_maxbytes': '67108864', 'accepting_conns': '1', 'listen_disabled_num': '0', 'time_in_listen_disabled_us': '0', 'threads': '4', 'conn_yields': '0', 'hash_power_level': '16', 'hash_bytes': '524288', 'hash_is_expanding': '0', 'slab_reassign_rescues': '0', 'slab_reassign_chunk_rescues': '0', 'slab_reassign_evictions_nomem': '0', 'slab_reassign_inline_reclaim': '0', 'slab_reassign_busy_items': '0', 'slab_reassign_busy_deletes': '0', 'slab_reassign_running': '0', 'slabs_moved': '0', 'lru_crawler_running': '0', 'lru_crawler_starts': '1', 'lru_maintainer_juggles': '56', 'malloc_fails': '0', 'log_worker_dropped': '0', 'log_worker_written': '0', 'log_watcher_skipped': '0', 'log_watcher_sent': '0', 'log_watchers': '0', 'unexpected_napi_ids': '0', 'round_robin_fallback': '0', 'bytes': '0', 'curr_items': '0', 'total_items': '0', 'slab_global_page_pool': '0', 'expired_unfetched': '0', 'evicted_unfetched': '0', 'evicted_active': '0', 'evictions': '0', 'reclaimed': '0', 'crawler_reclaimed': '0', 'crawler_items_checked': '0', 'lrutail_reflocked': '0', 'moves_to_cold': '0', 'moves_to_warm': '0', 'moves_within_lru': '0', 'direct_reclaims': '0', 'lru_bumps_dropped': '0'})]
```
