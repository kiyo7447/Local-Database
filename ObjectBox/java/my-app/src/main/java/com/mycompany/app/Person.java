package com.mycompany.app;

import io.objectbox.annotation.Entity;
import io.objectbox.annotation.Id;

@Entity
public class Person {
    @Id
    public long id;
    public String name;
    public int age;

    public Person() {
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
