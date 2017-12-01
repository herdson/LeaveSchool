from LineTracingModule import *
from trackingModule import *
from ultraModule import *

try:
    trackingModule = trackingModule()
    trackingModule.setup()

    LineTracingModule = LineTracingModule()
    LineTracingModule.setup()

except Exception:
    print("An error occurred while running the program.")
