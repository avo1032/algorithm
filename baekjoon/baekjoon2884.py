hour, minute = list(map(int, input().split()))

afterHour = hour
afterMinute = 0

if minute < 45:
    afterMinute = 60 - 45 + minute
    afterHour -= 1

if afterHour == -1 and minute < 45:
    afterHour = 23

if minute > 45:
    afterMinute = minute - 45

print(f'{afterHour} {afterMinute}')