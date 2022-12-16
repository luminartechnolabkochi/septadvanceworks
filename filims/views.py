from json import  load

with open("db.json","r",encoding="UTF-8") as f:
    data=load(f)
# print(data)

#print  filim names
filim_names=[filim.get("title") for filim in data]
# print(filim_names)


# print filimnames released in 2011
filims_11=[filim.get("title") for filim in data if filim.get("year")=="2011" ]
# print(filims_11)

# "Comedy" genres movies
com_movies=[filim.get("title") for filim in data if "Comedy" in filim.get("genres")]
# print(com_movies)

# which movie has longest runtime
long=max(data,key=lambda f:int(f.get("runtime")))
# print(long.get("title"))
# 1988:2,2000:4,2002:5


yc={} #{1988:1}
for f in data:
    year=f.get("year") #1988
    if year in yc:
        yc[year]+=1
    else:
        yc[year]=1

print(yc)



