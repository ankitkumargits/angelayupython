
# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)

#find another way

total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)