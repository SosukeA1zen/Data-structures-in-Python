def test(lst):
    result={}
    for item in lst:
        result[item[0]]=item[1:]
    return result

students=[[1,"Jean Castro","V"],[2,"Lula Powell Castro","V"],[3,"Brian Powell","V"]]
print(test(students))