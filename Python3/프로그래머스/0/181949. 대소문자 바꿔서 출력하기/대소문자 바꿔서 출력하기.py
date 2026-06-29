str = input()
r = ''

for i in str:
    if i.isupper() :
        r+= i.lower()
    else:
        r+= i.upper()
        
print(r)        