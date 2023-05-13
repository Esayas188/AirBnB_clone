# AirBnB Clone - The Console



**What’s a command interpreter?**

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to

be able to manage the objects of our project:

  

- Create a new object (ex: a new User or a new Place)

- Retrieve an object from a file, a database etc…

- Do operations on objects (count, compute stats, etc…)

- Update attributes of an object

- Destroy an object

  

### Learning Objectives

 - How to create a Python package
   
  - How to create a command interpreter in Python using the cmd module
   
   - What is Unit testing and how to implement it in a large project
   
   - How to serialize and deserialize a Class
   
   - How to write and read a JSON file
   
   - How to manage datetime
   
   - What is an UUID
   
   - What is *args and how to use it
   
   - What is **kwargs and how to use it
   
   - How to handle named arguments in a function

  
  

## Execution

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py

(hbnb)

Documented commands (type help <topic>):
========================================

EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

  
Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$

```

## Usage Examples

**Launching the console**
```
$ ./console.py
(hbnb) 
```
**Creating a new object**
```
(hbnb) create


(hbnb) create User

```
**Show an object**
```
(hbnb) show User


(hbnb) show User 
```
**Update an object**
```
(hbnb) all

(hbnb) update
(hbnb) all

```
**Destroy an object**
```
(hbnb) destroy
