name1= 'Sakib\'s khan'  #escape
name2= 'sakib khan'

#multiline string
name3= """
 sakib khan
 number one
          """

print(name1)

#string is a sequence of characters
for char in name2:
    print(char)

print(name2[3])  #3 no index a kon string ase dekhar jonno
print(name2[1:6])
print(name2)
print(name2[-3])
print(name2[::-1])  #last theke shob print hobe(reverse)

#mutable means changeable

#immutable means you cannot change it

print(name2)
if 'khan' in name2:  # total word er modhe ase kina for check
    print('exist')

print(name2.upper())    #string upper kora