from ob_model import Person, ob  # Corrected import statement

# Get the box for the Person entity.
box = ob.box_for(Person)

# Create a new person.
new_person_id = box.put(Person(first_name="Joe", last_name="Green"))

# Read a person.
person = box.get(new_person_id)
print(f'{person.first_name} {person.last_name}')

# Update a person.
person.last_name = "Black"
box.put(person)

# Delete a person.
box.remove(person)

# Cleanup.
ob.close()
