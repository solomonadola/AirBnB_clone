# AirBnB Clone Project

## Project Description
Welcome to the AirBnB clone project! This initiative involves crafting a command interpreter to manage AirBnB objects. The command interpreter empowers users to create, retrieve, update, and destroy objects, laying the foundation for the development of a comprehensive web application.

## Command Interpreter
The command interpreter, akin to a Shell, is customized for the efficient management of project objects. It facilitates actions such as creating new objects, retrieving objects from files or databases, and updating object attributes.

### Getting Started
To initiate the command interpreter, execute the main script.

```bash
./console.py
```

### Usage
The command interpreter supports a spectrum of operations:

- Create a new object
- Retrieve an object
- Perform operations on objects (count, compute stats, etc.)
- Update attributes of an object
- Destroy an object

### Examples
```bash
$ create User
$ show User 123
$ update User 123 email "new@example.com"
$ destroy User 123
```

## Development Information
This project is implemented using Python. Key components encompass a parent class (BaseModel) for object initialization and serialization, creation of AirBnB classes (User, State, City, Place, etc.), and integration of a file storage engine. Robust unit tests play a pivotal role in validating classes and the storage engine.

### Learning Objectives
Completion of this project equips you with proficiency in:

- Creating a Python package
- Developing a command interpreter using the cmd module
- Implementing unit testing in a large project
- Serializing and deserializing a class
- Reading and writing JSON files
- Managing datetime and UUID
- Understanding *args and **kwargs
- Handling named arguments in a function

## Requirements
- Python scripts are crafted and interpreted using Python 3.8.5 on Ubuntu 20.04 LTS.
- Permitted editors: vi, vim, emacs.
- Adherence to PEP8 style guide.
- All files are executable.
- Unit tests are devised employing the unittest module.

For detailed specifications, refer to the [project requirements](#).

## Unit Tests
Unit tests are systematically organized within the `tests` folder. Ensure that the test file structure mirrors the project structure.

### Running Tests
To execute all tests:

```bash
python3 -m unittest discover tests
```

For individual tests:

```bash
python3 -m unittest tests/test_models/test_base_model.py
```
