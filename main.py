import sys
from lesson4 import my_mod

file, work_time, tarif, bonus = sys.argv

my_mod.salary(int(work_time), int(tarif), int(bonus))
