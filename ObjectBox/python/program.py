import objectbox

import model

# from mypackage.model import Person

# Configure ObjectBox: should be done only once in the whole program and the "ob" variable should be kept around
model = objectbox.Model()
model.entity(Person, last_property_id=objectbox.model.IdUid(10, 1010))
model.last_entity_id = objectbox.model.IdUid(1, 1)
ob = objectbox.Builder().model(model).directory("db").build()

# Open the box of "Person" entity. This can be called many times but you can also pass the variable around
box = objectbox.Box(ob, Person)

id = box.put(Person(name="Joe Green"))  # Create
person = box.get(id)  # Read
person.name = "Joe Black"
box.put(person)       # Update
box.remove(person)    # Delete

