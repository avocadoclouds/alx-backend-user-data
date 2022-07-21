# 0x00-personal_data

### Resources
Read or watch:

What Is PII, non-PII, and Personal Data?
logging documentation
bcrypt package
Logging to Files, Setting Levels, and Formatting


### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

Examples of Personally Identifiable Information (PII)
How to implement a log filter that will obfuscate PII fields
How to encrypt a password and check the validity of an input password
How to authenticate to a database using environment variables

### Requirements
All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/env python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle style (version 2.5)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
All your functions should be type annotated

-----

#### Task 0
<img width="855" alt="image" src="https://user-images.githubusercontent.com/75071112/180319742-c68b6b89-534e-4c6b-b64e-19d81530ba98.png">


#### Task 1
<img width="864" alt="image" src="https://user-images.githubusercontent.com/75071112/180319928-2272955a-19b7-40b5-940e-d9e7b9bff1e8.png">


#### Task 2
<img width="864" alt="image" src="https://user-images.githubusercontent.com/75071112/180320003-cd3b705c-0344-40f6-93fd-c7865c564883.png">


#### Task 3
Database credentials should NEVER be stored in code or checked into version control. One secure option is to store them as environment variable on the application server.

In this task, you will connect to a secure holberton database to read a users table. The database is protected by a username and password that are set as environment variables on the server named PERSONAL_DATA_DB_USERNAME (set the default as “root”), PERSONAL_DATA_DB_PASSWORD (set the default as an empty string) and PERSONAL_DATA_DB_HOST (set the default as “localhost”).

The database name is stored in PERSONAL_DATA_DB_NAME.

Implement a get_db function that returns a connector to the database (mysql.connector.connection.MySQLConnection object).

Use the os module to obtain credentials from the environment
Use the module mysql-connector-python to connect to the MySQL database (pip3 install mysql-connector-python)

#### Task 4
Implement a main function that takes no arguments and returns nothing.

The function will obtain a database connection using get_db and retrieve all rows in the users table and display each row under a filtered format like this:

[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=e848:e856:4e0b:a056:54ad:1e98:8110:ce1b; last_login=2019-11-14T06:16:24; user_agent=Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN);
Filtered fields:

name
email
phone
ssn
password
Only your main function should run when the module is executed.


#### Task 5
