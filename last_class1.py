# import last_class as myFile1
# from last_class import myFunct,name

# myFunct('David')
# print(name)

# import datetime

# day = datetime.datetime.now()
# print(day.strftime("%H:%M:%S %p"))
# print(day.strftime("%Y%m%d"))

# f = open('onyi.txt', 'r')
# print(f.read())
# print(f.readlines())

# for x in f:
#     print(x)

# def myWrite():
#     file1 = open('demo.txt','w')
#     file1.write('Hello World')
#     print('File written successfully')
# myWrite()

# import os

# if os.path.exists('demof.txt'):
#     print('File exists')

# else:
#     print('File does not exist')



# open('demo.txt', 'w')

# with open('onyi.txt','a') as file1:
#     data = 'Wlecome to my profile!'
#     file1.write(data)



# data = []
# with open('demo.txt','r') as file2:
#     # myfile = file2.readlines()
#     # data.append(myfile)
#     for line in file2:
#         data.append(line.split(','))

# # for line in data:
# print(data)






# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was:{}'.format(x))


try:
    with open('demo.txt','r') as file:
        read_data = file.read()
        print(read_data)
except FileExistsError as file_error:
    # print('Couldn\'t open demo file')
    print(file_error)
