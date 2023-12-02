# 55816
# open input file
inpfile = open('input.txt', 'r')
lines = inpfile.readlines()
finsum = 0

# iterate through lines
for line in lines:
    nums = []
    for l in line:  
        if l.isdigit() is True:
            nums.append(int(l))
    finsum += int(nums[0]) * 10 + int(nums[len(nums)-1])

print(finsum)

            