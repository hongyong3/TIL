# 파일명 변경 금지
def swap(word):
    # 아래에 코드를 작성하시오.
    # word는 모두 알파벳으로만 구성되어 있습니다.
    ans = []
    for i in word:
        if ord(i) <= 90:
            j = chr(ord(i)+32)
            ans.append(j)
        if 97 <= ord(i) <= 122:
            j = chr(ord(i)-32)
            ans.append(j)
    return ''.join(ans)






# 아래의 코드는 출력 결과를 확인하기 위한 코드입니다.
# 수정하지마세요. 
if __name__ == '__main__':
    print(swap('KIM'))
    print(swap('python'))
    print(swap('UpperCamelCase'))