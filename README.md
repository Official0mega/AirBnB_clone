# AirBnB_clone Project
![img1](https://github.com/Official0mega/simple_shell/assets/122806822/31ee5cc0-3615-406b-a9c4-bc02b53fcdf2)

![img2](https://github.com/Official0mega/simple_shell/assets/122806822/f476be91-1386-41b0-ba71-8b404a0f3463)

## Description

* This  project aims to replicate some functionalities of the popular online accommodation marketplace, Airbnb.

* This typical "Airbnb_clone" project involves creating a web application or mobile application that allows users to list and book accommodations such as houses, apartments, or rooms for short-term stays. The project would generally consist of several key components and features, including:

* User Registration and Authentication:
Users should be able to create accounts, log in securely, and manage their profiles.

* Accommodation Listings:
Hosts should be able to create detailed listings for their properties, providing information about amenities, pricing, availability, and images.

* Search and Filters:
Users should be able to search for accommodations based on various criteria like location, dates, price range, number of guests, and amenities.

* Booking and Payments:
The application should facilitate the booking process, allowing guests to request reservations and hosts to confirm or decline them. Payment processing integration may be included to handle transactions securely.

* User Reviews and Ratings:
Guests should be able to leave reviews and ratings for the accommodations they've stayed in, and hosts should be able to respond to reviews.

* Messaging System:
A communication system that allows guests and hosts to exchange messages before and during the booking process.

* Notifications:
Users should receive email or in-app notifications for important events like new bookings, messages, and updates to their listings.

* Admin Panel:
An administrative interface to manage user accounts, listings, and handle reported issues.

* Responsive Design:
The application should be designed to work well on different devices, including desktops, tablets, and mobile phones.

**Note** To implement this project effectively, we typically use web development technologies such as HTML, CSS, JavaScript, and a backend framework like Django, Ruby on Rails, Node.js, or Flask. Database management systems like MySQL, PostgreSQL, or MongoDB are used to store the application data.

**Note** It's important to note that the specific features and complexity of the "Airbnb_clone" project can vary based on the developer's goals and requirements. It can be a great learning experience for aspiring web developers to practice building a real-world application, understanding user authentication, database management, and handling user interactions.


---


## The Command Interpreter

The command interpreter provides a simple REPL (Read-Evaluate-Print-Loop) for interacting with the models in this project only. It can be used to test the functionality of the supported storage engines as well. You can find some examples of its usage [here](#examples).

### How To Use

1. First clone this repository.

2. Once the repository is cloned locate the "[console.py](console.py)" file and run it as follows:
   ```powershell
   ➜  AirBnB_clone_v2 git:(main) ✗ ./console.py
   ```

4. When this command is run the following prompt should appear:
   ```
   (hbnb)
   ```

5. This prompt designates that you are in the "HBnB" console. There are a variety of commands available within the console program.

### Supported Commands

These are commands that can be executed by the command interpreter. They have the format `command [argument]...` but you could also use the format `Model.command([argument]...)`, with the exception of the first 3 commands below.

| Format | Description |
|:-|:-|
| `help [command]` | Prints helpful information about a command (`command`). If `command` is not provided, it prints the help menu. |
| `quit` | Closes the command interpreter. |
| `EOF` | Closes the command interpreter. |
| `create Model [prop_key=prop_value]...` | Creates a new instance of the `Model` class with the given properties. `prop_value` can be a double-quoted string with double-quotes escaped and spaces replaced with underscores. `prop_value` can also be a float or integer. |
| `count Model` | Prints the number of instances of the `Model` class. |
| `show Model id` | Prints the string representation of an instance of the `Model` class with the given `id`. |
| `destroy Model id` | Deletes an instance of the `Model` class with the given `id`. |
| `all [Model]` | Prints a list containing the string representation of all instances of the `Model` class. `Model` is optional and if it isn't provided, all the availble objects are printed. |
| `update Model id attr_name attr_value` | Updates an instance of the `Model` class with the given `id` by assigning the attribute value `attr_value` to its attribute named `attr_name`. Attributes having the names `__class__`, `id`, `created_at`, and `updated_at` are silently ignored. |
| `update Model id dict_repr` | Updates an instance of `Model` having the given `id` by storing the key, value pairs in the given `dict_repr` dictionary as its attributes. The keys `__class__`, `id`, `created_at`, and `updated_at` are silently ignored. |
<br>

### Supported Models

These are the models that are currently available.

| Class | Description |
|:-|:-|
| BaseModel | A(n abstract) class that represents the base class for all models (all models are instances of this class). |
| User | Represents a user account. |
| State | Represents the geographical state in which a _User_ lives or a _City_ belongs to. |
| City | Represents an urban area in a _State_. |
| Amenity | Represents a useful feature of a _Place_. |
| Place | Represents a building containing rooms that can be rented by a _User_. |
| Review | Represents a review of a _Place_. |

### Environment Variables

+ `HBNB_ENV`: The running environment. It can be `dev` or `test`.
+ `HBNB_MYSQL_USER`: The MySQL server username.
+ `HBNB_MYSQL_PWD`: The MySQL server password.
+ `HBNB_MYSQL_HOST`: The MySQL server hostname.
+ `HBNB_MYSQL_DB`: The MySQL server database name.
+ `HBNB_TYPE_STORAGE`: The type of storage used. It can be `file` (using `FileStorage`) or `db` (using `DBStorage`).

### Test Examples
###### Tests_1: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)
```

###### Tests_2: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959),
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)
```

###### Tests_3: Destroy an object

Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)
```
###### Tests_4: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889),
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Tests_5: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Tests_6: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Tests_7: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Tests_8: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>
<!-- ## Project Testing -->

# Before you push any commit, please run the script `./test.bash` to ensure that no tests are failing and your code complies with this project's styling standard.
