package com.mycompany.app;

import io.objectbox.Box;
import io.objectbox.BoxStore;
import io.objectbox.annotation.Entity;
import io.objectbox.annotation.Id;


import com.mycompany.app.Person;  // 生成された MyObjectBox クラスへのパス
// import com.mycompany.app.MyObjectBox;  // 生成された MyObjectBox クラスへのパス

public class App {
    public static void main(String[] args) {

        System.out.println( "Hello World!" );

        // Debug
        Person p = new Person("Alice", 30);
        System.out.println(p);


        // ObjectBoxの初期化
        BoxStore boxStore = MyObjectBox.builder().name("myDatabase").build();
        
        // PersonエンティティのBoxを取得
        Box<Person> personBox = boxStore.boxFor(Person.class);

        // 新しいPersonエンティティを作成して保存
        Person newPerson = new Person("Alice", 30);
        personBox.put(newPerson);

        // すべてのPersonエンティティを読み出し
        for (Person person : personBox.getAll()) {
            System.out.println(person);
        }

        // BoxStoreとの接続を閉じる
        boxStore.close();
    }
}
