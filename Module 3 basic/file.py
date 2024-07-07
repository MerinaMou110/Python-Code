# .csv  comma separated value
# .txt text file

# with open('messege.txt','w') as file:
#     file.write('I love you,python!')

# with open('messege.txt','a') as file:
#     file.write('I love you,python!')

with open('messege.txt','r') as file:
    text=file.read()
    print(text)