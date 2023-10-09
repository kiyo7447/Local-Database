import objectbox
from objectbox.model import Entity, Id, Model

@Entity  # 修正: id と uid の引数を削除
class Person:
    id = Id()  # 正しい id の定義
    first_name = str
    last_name = str

model = Model()
model.entity(Person)

ob = objectbox.Builder().model(model).build()
