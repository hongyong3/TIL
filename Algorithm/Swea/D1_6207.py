import sys
sys.stdin = open("D1_6207_input.txt", "r")

a = int(input())
ans = a * 1.8 + 32
# (0°C × 9/5) + 32 = 32°F
print(round(ans, 2))