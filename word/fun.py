text="hello hello hai hai hello"
# {hello:3,hai:2}
words=text.split(" ") #words=['hello', 'hello', 'hai', 'hai', 'hello']
wc={}#{hello:3,hai:2}

for w in words:#w=hai
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1
print(wc)

