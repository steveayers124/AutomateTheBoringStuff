# Print numbers 1 - 10 using a for loop
# Then print numbers 1 - 1- using a while loop

for num in range(10):
    print(num + 1)

num = 1
while num < 11:
    print(num)
    # num++           # It appears the ++ increment operator isn't valid in Python.
    num += 1
    # num = num + 1
# print('Whew! The loop is done.')
