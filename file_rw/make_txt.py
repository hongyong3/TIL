# #새로운 파일을 만들기 "new.txt",는 만드는 파일 이름 "w(쓰기)" "r(읽기)" 파일 용도
# # f. write("Hello !!!")에서 ("Hello !!!")는 쓰고싶은 내용
# # f.close() 파일을 닫는 코드

#방법1 (쓰기)
# f = open("new.txt", "w")
# f. write("Hello !!!")
# f.close()

#방법2 (쓰기)
# #with는 if와 같은거고, 끝나면 자동으로 close 해줌
# with open("new.txt", "w") as f:
#     f.write ("hugy !!!")


#방법1 (읽기)
# f = open("new.txt", "r")
# data = f.read()
# print(data)
# f.close()

#방법2 (읽기)
# with open("new.txt", "r") as f:
#     data = f.read()
#     print(data)



#여러줄
#다 쓴 다음에 f.close()를 4칸띄워쓰기를 한다면 닫기도 돌아가서 에러가 남/ 따라서 f.close()는 띄워쓰기를 하지 않고 쓰기
#글자가 깨질떄는 encoding='utf-8'을 써준다.

#방법1 (쓰기)
# f = open("new.txt", "w", encoding='utf-8')
# for i in range(5):
#     data = f"{i}번째 줄입니다.\n"
#     f.write(data)
# f.close()

# #방법2 (쓰기)
# with open("new.txt", "w", encoding= 'utf-8') as f:
#     for i in range(1, 5):
#         data = f"{i}번째 줄입니다.\n"
#         f.write(data)
# f.close()

#list 안의 요소들에 "요소이름\n"을 해주면 엔터처리가 된다
# menu = ["카레\n", "짬뽕\n", "탕수육\n"]
# f = open("menu.txt", "w", encoding= "utf-8")
# f.writelines(menu)
# f.close()

#여러줄 쓰기
# for in 구문을 쓸 떄는 range를 쓰자! ->range는 데이터 하나만 쓰고 list는 여러개의 데이터를 사용함

# with open("new.txt", "w", encoding = 'utf-8') as f:
#     for i in range(1, 6):
#         line = (f'이 줄은 {i}번 째 탭입니다.\t')
#         f.write(line)

# with open("new.txt", "w", encoding = 'utf-8') as f:
#     for i in range(1, 11):
#         data = f"{i}번째 줄입니다.\n"
#         f.write(data)

#readline으로 읽기
# with open("new.txt", "r", encoding = 'utf-8') as f:
#     line = f.readline()
#     print(line.strip())

# #readlines 파일 전체를 list 형태로 리턴
# with open("new.txt", "r", encoding = 'utf-8') as f:
#     lines = f.readlines()   ------> 모든 라인을 불러옴
#     for i in lines:
#         print(i.strip())