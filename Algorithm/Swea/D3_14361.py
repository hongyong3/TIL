import sys
sys.stdin = open("D3_14361_input.txt_input.txt", "r")

def permutation(arr, r):
    global xx
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    def generate(chosen, used):
        global permuArr
        if len(chosen) == r:
            if chosen[0] != '0':
                permuArr.append(int(''.join(chosen)))
            return
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)

T = int(input())
for test_case in range(T):
    N = int(input())
    arrN = list(str(N))
    permuArr = []
    permutation(arrN, len(arrN))
    ans = "impossible"
    for i in permuArr:
         if i > N:
            if i % N == 0:
                ans = "possible"
                break
    print("#{} {}".format(test_case + 1, ans))