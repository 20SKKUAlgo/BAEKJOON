M, D = map(int, input().split())

daysC = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

r = sum(daysC[:M])
r += D

print(days[r%7])