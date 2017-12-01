from LineTracingModule import *
from trackingModule import *
from ultraModule import *

try:
    ultraModule = ultraModule()
    ultraModule.setup()

    trackingModule = trackingModule()
    trackingModule.setup()

    LineTracingModule = LineTracingModule()
    LineTracingModule.setup()

except Exception:
    print("프로그램을 실행 중 문제가 발생했습니다.")
