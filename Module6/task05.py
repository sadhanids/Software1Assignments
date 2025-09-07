def numbers(my_list):
    second_list = [ num for num in my_list if num % 2 == 0]
    return second_list
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = numbers(original_list)

print(f"The original list is: {original_list}")
print(f"The filtered list is : {filtered_list}")
