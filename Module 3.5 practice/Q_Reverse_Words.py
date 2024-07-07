s=input()
words=s.split()
# print(words)
st=[]
for word in words:
    st.append(word[::-1])
print(*st)