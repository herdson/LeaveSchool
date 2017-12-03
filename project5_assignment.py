from LineTracingModule import *
from trackingModule import *
from ultraModule import *

try:
    trackingModule = trackingModule()
    trackingModule.setup()

    ultraModule = ultraModule()
    ultraModule.setup()

    LineTracingModule = LineTracingModule()
    LineTracingModule.setup(trackingModule, ultraModule)

except Exception as e:
    print("(PR) An error occurred while running the program.")
    print(e)