import random
import objectbox

import model

# from mypackage.model import Person

# Configure ObjectBox: should be done only once in the whole program and the "ob" variable should be kept around
db_model = objectbox.Model()
db_model.entity(model.Person, last_property_id=objectbox.model.IdUid(10, 1010))
db_model.last_entity_id = objectbox.model.IdUid(1, 1)
ob = objectbox.Builder().model(db_model).directory("db").build()

# Open the box of "Person" entity. This can be called many times but you can also pass the variable around
box = objectbox.Box(ob, model.Person)

# 以下のPersonの部分を修正
person = model.Person()
person.name = "Joe Higashi"
id = box.put(person)  # Create
print(f"Joe person.id={person.id}, name={person.name}")

person = model.Person()
person.name = "Duck King"
person.is_enabled = True
person.int64 = 64
person.int32 = 32
person.int16 = 16
person.int8 = 8
person.float64 = 64.64
person.float32 = 32.32
person.byte_array = b"byte array"
person.transient = "transient"
id = box.put(person)  # Create
print(f"Duck person.id={person.id}, name={person.name}")

person = box.get(id)  # Read
person.name = "JTung Fu Rue"
box.put(person)       # Update

if random.random() < 1/3:
    box.remove(person)    # Delete


# 一覧の取得
all_persons = box.get_all()

# 結果を表示
for person in all_persons:
    print(f"ID: {person.id}, Name: {person.name}, is_enabled: {person.is_enabled}, int64: {person.int64}, int32: {person.int32}, int16: {person.int16}, int8: {person.int8}, float64: {person.float64}, float32: {person.float32}, byte_array: {person.byte_array}, transient: {person.transient}")

if random.random() < 1/50:
    box.remove_all()   # Delete all


# id = box.put(model.Person(name="Joe Green"))  # Create
# person = box.get(id)  # Read
# person.name = "Joe Black"
# box.put(person)       # Update
# box.remove(person)    # Delete
