# name="programming"
# for i in range(len(name)-1,-1,-1):
#     print(name[i],end=" ")

name="programming"
reverse=""
for i in range(len(name)-1,-1,-1):
    reverse=reverse+name[i]
print(reverse)