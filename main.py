# Задача 22
# a = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
# b = [3, 6, 9, 12, 15, 18]
# a = set(a)
# b = set(b)
# c = a.intersection(b)
# c = list(c)
# c.sort()
# print(*c)

# Задача 24
# a = [5, 6, 7, 2, 3, 9]
# i_max = -1
# sum_max = a[-2]+ a[-1] + a[0]
# for i in range(len(a)-1):
#     cur_sum = a[i-1]+a[i]+a[i+1]
#     if cur_sum>sum_max:
#         sum_max = cur_sum
#         i_max = i
# print(sum_max, i_max)