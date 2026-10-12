import sys, importlib
from common import copy_assets, OUT
copy_assets()
mods = sys.argv[1:] or ["p1","p2","p3","p4","p5","p6","p7","p8","p9","p10"]
for m in mods:
    importlib.import_module(m).build(); print("built", m)
print(OUT)
