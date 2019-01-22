import sys
sys.stdin = open("특별한정렬_input.txt")

def select(data):
    for i in range(0, len(data)):
        m_Index = i
        if m_Index % 2:
            for j in range(i+1, len(data)):
                if data[m_Index] > data[j]:
                    m_Index = j
            data[i], data[m_Index] = data[m_Index], data[i]

        else:
            for j in range(i+1, len(data)):
                if data[m_Index] < data[j]:
                    m_Index = j
            data[i], data[m_Index] = data[m_Index], data[i]
    return ' '.join(str(i) for i in data[0:10])


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    print("#{} {}".format(test_case, select(data)))

