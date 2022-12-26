def returnsum(myDict):
    list=[]
    for i in myDict:
             list.append(myDict[i])
    final=sum(list)
    return final
dict={'a':200,'b':300,'c':400}
print("sum:",returnsum(dict))
