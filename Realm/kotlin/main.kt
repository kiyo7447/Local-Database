import io.realm.Realm
import io.realm.RealmConfiguration

fun main() {

// Define the Realm configuration
val config = RealmConfiguration.Builder()
    .name("myrealm.realm")
    .schemaVersion(1)
    .build()

// Initialize Realm
val realm = Realm.getInstance(config)

// Define a data model
open class Person(
    var name: String = "",
    var age: Int = 0
) : RealmObject()

// Add data to Realm
realm.executeTransaction { realm ->
    val person = realm.createObject(Person::class.java)
    person.name = "John"
    person.age = 25
}

// Query data from Realm
val results = realm.where(Person::class.java)
    .equalTo("name", "John")
    .findAll()

// Update data in Realm
realm.executeTransaction { realm ->
    results[0]?.age = 26
}

// Delete data from Realm
realm.executeTransaction { realm ->
    results.deleteAllFromRealm()
}

// Close Realm when done
realm.close()
}
