def uncommon_list(ls1,ls2):
    i=0
    new_list=[]
    for i in ls1:
        if i not in ls2:
            new_list.append(i)
    for j in ls2:
        if j not in ls1:
            new_list.append(j)
    print(new_list)

list1 = [1, 1, 2]
list2 = [2, 3, 4]
list3 = [1, 1, 2, 3, 4, 2]
list4 = [1, 3, 4, 5]
uncommon_list(list1,list2)
uncommon_list(list3,list4)
