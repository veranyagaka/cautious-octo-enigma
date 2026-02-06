nums = [8, 1, 2, 2, 3]
output = []
for i in range(len(nums)):
    count = 0
    for j in range(1, len(nums)):
        if nums[j] < nums[i]:
            count += 1

    output.append(count)

print(output)
