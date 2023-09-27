# numbers = [100, 2, 3, 4, 5]


# # 맥스
# # # = max([1, 2, 3, 4, 5])
# max_num = max(numbers)
# # print(max_num)


# # 랜덤
import random
# random_number = random.randint(1, 100)
# # 랜덤이라는 도구상자 안에서 랜드인트라는 함수를 꺼내올 때 . 사용
# print(random_number)


# #
# menus = ['pizza', 'bread', 'burger']
# random_menu = random.randint(0, 2)
# print(menus[random_menu])


# # choice
# menu = random.choice(menus)
# print(menu)

# numbers = range(1, 46)
# lucky_number = random.choice(numbers)
# print(lucky_number)

#############################

# # sample 로또번호 랜덤추출 (한 번에 6개 추출)
# 1. 무작위 배열
numbers = range(1, 46)
lucky_number = random.sample(numbers, 6)
# print(lucky_number)
# # 2. 순서대로 배열 (sorted)
# print(sorted(lucky_number))

# URL
URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086'

# pip install requests
import requests

res = requests.get(URL)
data = res.json() #스트링을 딕셔너리구조로 바꿈 >> 키값을 이용해 데이터에 접근 가능

drwtNo1 = data['drwtNo1']
drwtNo2 = data['drwtNo2']
drwtNo3 = data['drwtNo3']
drwtNo4 = data['drwtNo4']
drwtNo5 = data['drwtNo5']
drwtNo6 = data['drwtNo6']
# print(drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6)
# print(data['drwNoDate'])

lotto_number = [drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6]

print(lucky_number)
print(lotto_number)

print(set(lucky_number) & set(lotto_number))