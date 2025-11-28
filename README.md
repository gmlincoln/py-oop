## 📘 Python OOP – Complete Guide
- This repository provides a complete introduction to Object-Oriented Programming (OOP) in Python, covering all core concepts with examples, exercises, and mini–projects.  
- Perfect for beginners, students, and interview preparation.

### What is OOP?

- Object-Oriented Programming (OOP) is a programming paradigm where code is organized around objects — data + behavior.
- Why use OOP? 
- Increases reusability 
- Keeps code clean and organized 
- Easier to maintain large  
- Makes code modular and scalable 

### 🧱 Core Concepts of OOP

#### 1️⃣ Class
A class is a blueprint for creating objects.

```python
class Person:
    pass

```

#### 2️⃣ Object (Instance)
An object is created from a class.

```python
class Person:
    pass

p = Person()

```

#### 3️⃣ Attributes & Methods

```python
class Person:
    def __init__(self, name, age):   # constructor
        self.name = name             # attribute
        self.age = age

    def speak(self):                 # method
        return f"My name is {self.name}"

```
<!-- 
```python

```

```python

```
```python

```
```python

``` -->
### NEXT CLASSS TOPIC

#### 4️⃣ Encapsulation
Hiding internal data and controlling access.

```python

```
#### 5️⃣ Inheritance
Creating a new class using an existing class.

```python

```
#### 6️⃣ Polymorphism
Same method name, different behavior.

```python

```
#### 7️⃣ Abstraction
Hiding complexity and showing only the essentials.

```python

```

#### 8️⃣ Composition
Using one class inside another – “has-a” relationship.

<!-- ```python
class Engine:
    pass

class Car:
    def __init__(self, engine):
        self.engine = engine

``` -->

#### 9️⃣ Dunder (Magic) Methods
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

```


### 📝 Practice Tasks 
- Create Student, Book, Employee classes 
- Build a Calculator class 
- Implement Shape → Circle & Rectangle → area() 
- Create a Bank account system (deposit/withdraw) 
- Build a Library system (add/find books)