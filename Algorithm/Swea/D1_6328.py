import sys
sys.stdin = open("D1_6328_input.txt", "r")

def solve(seq1, seq2):
    if len(seq1) > len(seq2):
        print(seq1)
    else:
        print(seq2)

seq1, seq2 = map(str, input().split(', '))
solve(seq1, seq2)
