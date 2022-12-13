# time_pause

This python library serves to pause the time just like Za Warudo from Jojo

## installation

```pip install time_pause```

## usage
```python
import time_pause
# or
from time_pause import *

time_p = time_pause.time_p()
# or
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
time_pause.pause() # unpaused
```
