import sys
from datetime import time
sys.stdin = open("D1_6308_input.txt", "r")

name = str(input())
age = int(input())
print("{}(은)는 {}년에 100세가 될 것입니다.".format(name, datetime.today().year + 80))