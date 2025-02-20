name = input("Name: ")
nums = []

for i in name:
    nums.append(ord(i.lower()) - 96)

print(nums)
