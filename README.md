# timeutilities

Description
-----------
timeutilities is for time manipulation and management with classes designed for handling multiple time functions.

Installation
-------
```bash
pip3 install timeutilities
```

Examples
---------
- Get current time
```python
from timeutilities import Time
now = Time.now()
```
- From DateTime
```python
from timeutilities import Time
from datetime import datetime
now = Time.from_datetime(datetime.now())
```
- Arithmetic operations
```python
from timeutilities import Time
from time import sleep
previous_time = Time.now()
sleep(5)
current_time = Time.now()
#Addition
total_time = current_time + previous_time
print(total_time)
#Subtraction
difference = current_time - previous_time
print(total_time)
#Comparison
print(current_time > previous_time)
print(current_time < previous_time)
print(current_time >= previous_time)
print(current_time <= previous_time)
```
Documentation
----------------
~~Availiable at http://astraldev.github.io/timeutilities~~

