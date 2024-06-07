# f=open('python.txt','r',enconding="UTF-8")
f=open('python.txt')
content = f.readlines()
# ['hello word\n', 'abcdefg\n', 'aaa\n', 'bbb\n', 'ccc']
print(content)
#关闭文件
f.close()

f=open('python.txt')
content=f.readline()
print(f'第一行:{content}')
content=f.readline()
print(f'第二行:{content}')
f.close()