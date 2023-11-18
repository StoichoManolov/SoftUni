address = input().split("\\")

file = address[-1]

file_name, extension = file.split('.')

print(f'File name: {file_name}')
print(f'File extension: {extension}')
#
# string = input().split('\\')
#
# file_name, extension = string[-1].split('.')
#
# print(f'File name: {file_name}')
# print(f'File extension: {extension}')
