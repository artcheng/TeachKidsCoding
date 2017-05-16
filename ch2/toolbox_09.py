# in python, there are a lot of tool box available, we normally call them module

# you could either use the whole toolbox
import time
current = time.time()  # get system time in seconds
print current

import math
print math.sqrt(2.0)



# or you could use a piece of tool in a toolbox
from random import randint
x = randint(0,9)
print x

from datetime import datetime  # the first datetime is the name of the module (toolbox), the second datetime is a class (piece of tool) in the module
now = datetime.now()
print now



