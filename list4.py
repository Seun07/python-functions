def sum():

    list=[10,20,30,40,50,60,80,90]
    #print(sum(list))
    total=0
    for i in list:
        #print(i)
        total=total+i
    print(total)
    if total>500:
        print("It is greater than 500")
        q=total*50
        print(q)
    else:
        print("oh no its less than 500")
        q=total-50
        print(q)
sum()