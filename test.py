# for i in range(11):
#     for x in range(11):
#         times = i * x
#         print('{} x {} = {}'.format(i, x, times))
#     print()

# x = divmod(2500, 300)
# print("devmod ", x)


# word_count = 2500
# words_per_page = 275  # Assuming 275 words per page
# estimated_pages = word_count / words_per_page

# print(f"Estimated number of pages: {estimated_pages:.2f}")

# function definition
def get_square(num):
    return num * num

for i in [1,2,3]:
    # function call
    result = get_square(i)
    print('Square of',i, '=',result)
