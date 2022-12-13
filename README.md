# time_pause

This python library serves to pause the time just like Za Warudo from Jojo

## installation

```pip install time_pause```

## usage
```python
import time_pause
time_p = time_pause.time_p()
# or
from time_pause import *
time_p = time_p()
```

## how do i access to the current time????

```python
print(time_p)
# prints the current time
time = time_p.__float__() # makes sure to get the float value
timestr = time_p.__str__() # makes sure to get the value to string
```

## then how do i pause and unpaused the time?

```python
time_p.pause() # paused
time_p.pause() # unpaused
```
# How to test if the module works?

First of all get the filez where the module is:
```python
import time_pause, os
print(os.path.dirname(time_pause.__file__))
```
then open the file and run it like any other python script.<br/> a window should appears

# what are ,,__PRIVATE__'' functions in the class?

Functions that begins with **__PRIVATE__** are used by the class to do special stuff that can't be done without a function.
