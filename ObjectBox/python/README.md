
### 公式ドキュメント
https://docs.objectbox.io/

https://objectbox.io/offline-first-mobile-database/
### ObjectBox Python 参考
https://github.com/objectbox/objectbox-python

# 動作の仕方
## インストール
```
wsl
pip install --upgrade objectbox
```
## 実行１
```
make depend
// Activate virtual environment...
// ...on Linux
source .venv/bin/activate
// ...on Windows
.venv\Scripts\activate


// Run the example
python3 -m example

// Once done, leave the virtual environment
deactivate
```
## 実行２
### モデルの作成
モデルは、@Entityデコレータで注釈が付けられた Python クラスで構成されます。
```
python3 program.py 
```
### 結果
```
kiyo@DrifterMiniPC:/mnt/c/dev/GitHub/kiyo7447/Local-Databases/ObjectBox/python$ python3 program.py 
Joe person.id=8, name=Joe Higashi
Duck person.id=9, name=Duck King
ID: 1, Name: Joe Higashi, is_enabled: False, int64: 0, int32: 0, int16: 0, int8: 0, float64: 0.0, float32: 0.0, byte_array: b'', transient:        
ID: 2, Name: Joe Higashi, is_enabled: False, int64: 0, int32: 0, int16: 0, int8: 0, float64: 0.0, float32: 0.0, byte_array: b'', transient:        
ID: 3, Name: Joe Higashi, is_enabled: False, int64: 0, int32: 0, int16: 0, int8: 0, float64: 0.0, float32: 0.0, byte_array: b'', transient:        
ID: 4, Name: Joe Higashi, is_enabled: False, int64: 0, int32: 0, int16: 0, int8: 0, float64: 0.0, float32: 0.0, byte_array: b'', transient:        
ID: 5, Name: Joe Black Higachi, is_enabled: False, int64: 0, int32: 0, int16: 0, int8: 0, float64: 0.0, float32: 0.0, byte_array: b'', transient:  
ID: 6, Name: Joe Higashi, is_enabled: False, int64: 0, int32: 0, int16: 0, int8: 0, float64: 0.0, float32: 0.0, byte_array: b'', transient:        
ID: 7, Name: Joe Higashi, is_enabled: False, int64: 0, int32: 0, int16: 0, int8: 0, float64: 0.0, float32: 0.0, byte_array: b'', transient:        
ID: 8, Name: Joe Higashi, is_enabled: False, int64: 0, int32: 0, int16: 0, int8: 0, float64: 0.0, float32: 0.0, byte_array: b'', transient:        
ID: 9, Name: JTung Fu Rue, is_enabled: True, int64: 64, int32: 32, int16: 16, int8: 8, float64: 64.64, float32: 32.31999969482422, byte_array: b'byte array', transient:
```
# TODO
動作していない。⇒動かした。
