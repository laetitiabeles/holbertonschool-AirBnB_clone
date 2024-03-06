<p align="center"> 
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240304%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240304T160716Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cf6fca83fcce1349c1281c9ee82cae5ce41e58fb101fce938a7578640d0692bb" alt="HolbertonBnB logo">
</p>

______________________________________________________________________________________________________________________________
<h1 align="center" >
<br>
    <img src="https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg" height="50%" width="30%">
</h1>

<h2 align="center">
    AirBnB (clone)
</h2>

<p align="center">
<img src="https://user-images.githubusercontent.com/68792144/141602345-7b71c4ea-a4dd-42d9-b706-7fc2c7b85ca5.png" height="50%" width="20%">
</p>

<h4 align="center"> This project is WepApp in Python </h4>

<p align="center">
    <a href="#Description">Description</a> •
    <a href="#The console">The console</a> •
    <a href="#Classes">Classes</a> •
    <a href="#Files ">Files </a> •
 <a href="#Execution ">Execution </a> •
  <a href="#Commands ">Commands </a> •
  <a href="#Autors">Autors</a> •

</p>

---


____________________________________________________________________________________________________________________________
# Description
This project is the first step of the AirBnB project, which is an AirBnB clone that includes design, layout, infrastructure and database.
The project currently only implements the back-end console.
We will not implement all the features, just some of them to cover all the fundamental concepts of the higher level programming track.

_____________________________________________________________________________________________________________________________
# Overview
This is first step for the project AirBnB-Clone called ´The console´.
First we create a command line interpreter like we did in Shell Project.
Then we have to manage Classes in order to create, show, update and destroy objects.

______________________________________________________________________________________________________________________________
# The console

<p align="center"><img src="https://user-images.githubusercontent.com/68792144/141602516-90e36740-e66e-4edd-8baf-08f318b10a58.png" width="700"></p>

______________________________________________________________________________________________________________________________
# Classes :

HolbertonBnB utilizes the following classes:


|     | BaseModel | FileStorage | User | State | City | Amenity | Place | Review |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| **PUBLIC INSTANCE ATTRIBUTES** | `id`<br>`created_at`<br>`updated_at` | | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` |
| **PUBLIC INSTANCE METHODS** | `save`<br>`to_dict` | `all`<br>`new`<br>`save`<br>`reload` | "" | "" | "" | "" | "" | "" |
| **PUBLIC CLASS ATTRIBUTES** | | | `email`<br>`password`<br>`first_name`<br>`last_name`| `name` | `state_id`<br>`name` | `name` | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` | 
| **PRIVATE CLASS ATTRIBUTES** | | `file_path`<br>`objects` | | | | | | |


______________________________________________________________________________________________________________________________
# Files

| File | Description |
|--|--|
| **AUTHORS** | Contains the authors of the AirBnB-Clone Project. |
| **README.md** | Contains an overview of AirBnB-Clone Project. Important things that you should know before executes our AirBnB-Clone command line program. |
| **console.py** |  **HBNBCommand:** Class that defines the command line interpreter. **do_EOF:** command to exit the program. **do_quit:** command to exit the program. **emptyline:** when the line is empty does not perform any action. **do_precmd:** parses command input **help_help:** Prints help command description. **do_create:** Creates a new instance of BaseModel. **do_show:** Prints the string representation of an instance. **do_destroy** Deletes an instance based on the class name and id. **do_all** Prints all string representation of all instances. **do_update** Updates an instance by adding or updating its attribute. **do_count** counts number of instances of a class. |
| **models** | **engine** file storage directory. **__init__.py ** Create a unique FileStorage instance for your application. **amenity.py ** Class based on BaseModel. **base_model.py ** Base class that defines all common attributes/methods for other classes. **city.py ** Class based on BaseModel. **place.py ** Class based on BaseModel. **review.py ** Class based on BaseModel. **state.py ** Class based on BaseModel. **user.py ** Class based on BaseModel. |
| **tests** | **test_models** Test files directory. **__init__.py ** Packages the tests files. |




├── AUTHORS
├── README.md
├── console.py
├── file.json
├── models
│   ├── __init__.py
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── __init__.py
│   │   └── file_storage.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
└── tests
    ├── __init__.py
    └── test_models
        ├── __init__.py
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_engine
        │   ├── __init__.py
        │   └── test_file_storage.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py

______________________________________________________________________________________________________________________________
# Execution
`Interactive Mode`
 ```shell
 $ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
 ```
`Non-Interactive Mode`
```shell
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
______________________________________________________________________________________________________________________________
| Command | Description |
| -------| ----------- |
| `quit` | Quits the console |
| `EOF` | Quits the console |
| `help` | Displays help page |
| `create <class>` | Creates a new instance of a given class with a unique ID and saves it to a JSON file |
| `show <class> <id>` | Prints the string representation of a class instance based on the class name and ID|
| `destroy <class> <id>` | Deletes and instance based on the class name and id and saves it to a JSON file |
| `all` | Prints all string representation of all instances based or not on the class name |
| `update` | Updates an instance based on the class name and id by adding or updating attribute and saves changes to a JSON file |

______________________________________________________________________________________________________________________________
## <p align="center">Authors</p>

# <p align="center">[Laëtitia BELES ](https://github.com/laetitiabeles/holbertonschool-AirBnB_clone/tree/features/models/models)</p>


# <p align="center">[Mhamed ABDELMALEK ](https://github.com/laetitiabeles/holbertonschool-AirBnB_clone/tree/features/models/models)</p></p>


