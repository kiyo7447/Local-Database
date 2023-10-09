import objectbox

# Define the model
model = objectbox.Model()
entity = model.entity('Person', last_property_id=10, last_index_id=1)
entity.id = 1
entity.add(objectbox.Property('name', objectbox.PropertyType.string))
entity.add(objectbox.Property('age', objectbox.PropertyType.int32))

# Create the database and box
ob = objectbox.Builder().model(model).directory("db").build()
box = ob.box('Person')

# Create a person and store it in the database
person = {'name': 'John Doe', 'age': 30}
person_id = box.put(person)

# Retrieve the person from the database
person = box.get(person_id)
print(person)
