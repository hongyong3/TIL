# "C:\Users\student\Desktop\TIL\dummy"는 절대 주소  // 현재 위치가 그자리면 "."
#import os
#os. chdir(r"C:\Users\student\Desktop\TIL\dummy")
#리스트를 데릭 와야함 // 이미 'chdir'로 위치를 이동했으닌까 현재위치 = . 임// 변수는 이름 하나 지정해주는 것임 filename은 자기 마음대로 해도 됨. / 단, 단수로
#for filename in os.listdir("."):
#    os.rename(filename, "SAMSUNG " + filename)


#파일명 바꾸기
# import os
# os. chdir(r"C:\Users\student\Desktop\TIL\dummy")
# for filename in os.listdir("."):
#     os.rename(filename, filename.replace("SSAFY SSAFY ", "SSAFY ")) 

