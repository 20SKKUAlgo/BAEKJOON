# https://stultus.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-2869-%EB%8B%AC%ED%8C%BD%EC%9D%B4%EB%8A%94-%EC%98%AC%EB%9D%BC%EA%B0%80%EA%B3%A0-%EC%8B%B6%EB%8B%A4

# 관계식을 잘 세워야 한다 ㅠㅛㅠ

a, b, v = map(int, input().split())

day = (v-b)/(a-b)
print(int(day) if day == int(day) else int(day)+1)