let myDog = Dog()
myDog.name = "Fido"
myDog.age = 3

// データを保存
let realm = try! Realm()
try! realm.write {
    realm.add(myDog)
}

// データを取得
let dogs = realm.objects(Dog.self)
for dog in dogs {
    print("\(dog.name) is \(dog.age) years old")
}

// データを削除
try! realm.write {
    realm.delete(myDog)
}
