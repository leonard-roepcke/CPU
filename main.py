print("CPU started")

from utils import *

#a = Safe_8bit([1,0,0,0,0,0,0,1])
#b = Safe_8bit([1,0,0,0,0,0,0,1])
#print(add_8bit(a.read(), b.read()))

print("Cnt")
cnt = Cnt()
print(cnt.read())

cnt.tick()
print(cnt.read())

cnt.tick()
print(cnt.read())

cnt.tick()
print(cnt.read())
