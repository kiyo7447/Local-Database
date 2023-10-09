# ObjectBoxをインポート
import objectbox

# モデルを定義（ここでは、例としてPersonクラスを作成）
class Person(objectbox.Model):
    id: int
    first_name: str
    last_name: str

# ObjectBoxインスタンスを作成
ob = objectbox.Builder().model(Person).build()

# Entity Boxを取得
box = ob.box_for(Person)

# レコードを作成して保存
joe_id = box.put(Person(first_name="Joe", last_name="Green"))

# レコードを読み取る
joe = box.get(joe_id)

# レコードを更新
joe.last_name = "Black"
box.put(joe)

# レコードを削除
box.remove(joe)
