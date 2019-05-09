# 파일명 변경 금지
def anti_vowel(word):
    # 아래에 코드를 작성하시오.
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        word = word.replace(vowel, '')
    return word





# 아래의 코드는 출력 결과를 확인하기 위한 코드입니다.
# 수정하지마세요. 
if __name__ == '__main__':
    print(anti_vowel('bye, aeiou'))
    print(anti_vowel('apple'))
    print(anti_vowel('py'))