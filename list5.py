def total():

#Write a python code that will add list of numbers together
    list1=[1,2,4,6,7,9,10]
#print(sum(list1))
    total=0
    for i in list1:
        #print(i)
        total=total+i
        #print(total)
        if total ==20:
            print("print total is", total)
            c=total*50
            print("Total is now", c)
total()