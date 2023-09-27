# 1. apple / Apple
# 2. git add. / git add .
# 3. message / massage


# 1. 저장
# 변수, variable 
# 자주 쓸 데이터 형태 (할당될 수 있는 데이터의 형태) 3가지
# 1. 숫자(int)
# dust = 10
# 2. 글자(string)
# dust = '100'
# 3. 참/거짓 (boolean) 
# dust = True /# False

# # dust_list = [10, 20, 0, 100]

# dust_dict = {
#     '서울': 100,
#     '대전': 10,
#     '부산': 50
# }
# # print(dust_dict)





# # # 2. 조건
# # age = 20

# # if age > 20:
# #     print('성인입니다.')
# # elif age > 8:
# #     print('급식입니다.')
# # else:
# #     print('어린이입니다.')


# dust = 150

# if dust > 150:
#     print('매우나쁨')
# elif dust > 80:
#     print('나쁨')
# elif dust > 30:
#     print('보통')
# else:
#     print('좋음') 

# if 150 <= dust
#     print('very bad')
# elif 80 <= dust < 150:
#     print('bad')
# elif 30 <= dust and dust < 80:
#     print('average')
# else:
#     print('good')




# 3. 반복
menus = ['pizza', 'hamburger', 'sandwiches', 'coke']

# index접근. 순서대로.
n = 0
while n < 4:
    print(menus[n])
    n = n + 1

# 범위(수량)을 정해주는 코드 (전체 데이터를 조각내서 나열)
# for item in list
for menu in menus:
    print(menu)
