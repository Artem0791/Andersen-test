new_array = [i for i in range(100)]
check_array = []
for i in new_array:
    if i % 3 == 0:
        check_array.append(i)
    else:
        continue
print(check_array)
