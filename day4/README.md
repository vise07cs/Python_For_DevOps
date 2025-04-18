# Python Functions, Modules and Packages

## 1. Differences Between Functions, Modules, and Packages

### Functions

A function in Python is a block of code that performs a specific task. Functions are defined using the `def` keyword and can take inputs, called arguments. They are a way to encapsulate and reuse code.
Python interpreter understands looking at `def` that its a function. 

Benefits of functions:
1 -->  increases readiblity
2 --> re - usability or modularity
3 --> Debugging is easier 



**Example:**

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)
```

In this example, `greet` is a function that takes a `name` argument and returns a greeting message.

### Modules

A module is a Python script containing Python code. It can define functions, classes, and variables that can be used in other Python scripts. Modules help organize and modularize your code, making it more maintainable.

module == group of functions 

**Example:**

Suppose you have a Python file named `my_module.py`:

```python
# my_module.py
def square(x):
    return x ** 2

pi = 3.14159265
```

You can use this module in another script:

```python
import my_module

result = my_module.square(5)
print(result)
print(my_module.pi)
```

In this case, `my_module` is a Python module containing the `square` function and a variable `pi`.

### Packages

A package is a collection of modules organized in directories. Packages help you organize related modules into a hierarchy. They contain a special file named `__init__.py`, which indicates that the directory should be treated as a package.

package== collection of modules

**Example:**

Suppose you have a package structure as follows:

```
my_package/
    __init__.py
    module1.py
    module2.py
```

You can use modules from this package as follows:

```python
from my_package import module1

result = module1.function_from_module1()
```

In this example, `my_package` is a Python package containing modules `module1` and `module2`.
So if you know your module is goinf to be used by other team members its always a good practice to push the module to a PYPI( Python package index )
you can download modules form PYPI modules and packages.(Google --> pypi-->search for modules) .
pip install boto3
pip install github

pip list --> to see all the list of modules installed 
## 2. How to Import a Package

Importing a package or module in Python is done using the `import` statement. You can import the entire package, specific modules, or individual functions/variables from a module.

**Example:**

```python
# Import the entire module
import math

# Use functions/variables from the module
result = math.sqrt(16)
print(result)

# Import specific function/variable from a module
from math import pi
print(pi)
```

In this example, we import the `math` module and then use functions and variables from it. You can also import specific elements from modules using the `from module import element` syntax.

## 3. Python Workspaces

Python workspaces refer to the environment in which you develop and run your Python code. They include the Python interpreter, installed libraries, and the current working directory. Understanding workspaces is essential for managing dependencies and code organization.

Python workspaces can be local or virtual environments. A local environment is the system-wide Python installation, while a virtual environment is an isolated environment for a specific project. You can create virtual environments using tools like `virtualenv` or `venv`.

Each project should have  a seperate virtual Environment (#good_practice)
modules installed on one virtual env will not be reflected in other virtual env
pip install virtualenv

**Example:**

```bash
# Create a virtual environment
pip install virtualenv


python -m venv project_name

# Activate the virtual environment (on Windows)
project_name\Scripts\activate

# Activate the virtual environment (on macOS/Linux)
source project_name/bin/activate


pip install module_name

pip show module_name 
# DeActivate the virtual environment
 deactivate

# To delete the virtual env
 rmdir .\project_name\
```

Once activated, you work in an isolated workspace with its Python interpreter and library dependencies.
 On activation, your command prompt will typically show the name of the virtual environment in parentheses.

to come out --> use command --> deactivate

