from LineTracingModule import *
from trackingModule import *

try:
    trackingModule = trackingModule()
    trackingModule.setup()

    LineTracingModule = LineTracingModule()
    LineTracingModule.setup(trackingModule)

except Exception as e:
    print("(PR) An error occurred while running the program.")
    print(e)
