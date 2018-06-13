def frequency(books):
    '''(2d_list)-->2d_list'''
    f=[]
    nb=books
    for i in range(len(books)):
        flag=False
        for j in range(len(f)):
            if books[i][1]==f[j][0]:
                f[j][1]=f[i][1]+1
                flag=True
        if not flag:
            f.append([books(i[1],1)])
            frequency3(q)
    return f


from collections import Counter

def frequency2(x):
    file=open("bestsellers.txt", "r")
    f=[]
    f.append([[x], 1])
    for i in file.read().split():
        if i not in f:
            f[i] = 1
        else:
            f[i] += 1
    print (i,f)
    file.close()
    return f
            

def frequency3(q):
    file=open("bestsellers.txt", "r")
    f={}
    for q in file.read().split():
        if q not in f:
            f[q[1]] = 1
        else:
            f[q[1]] += 1
    print (q,f)
    file.close()


def frequency4(x):
    a=input('enter integer')
    f=[]
    for i in x:
        if a in i[1].lower():
            frequency3(q)
            f[q] = 1
        else:
            f[q] += 1


text=open("bestsellers.txt")
count=0
x=[]
for i in text:
    ilist=i.split("\t")
    x.append(ilist)

c=1
while c==1:
    print("What would you like to do? Enter 1, 2, 3, 4, 5, 6 or Q for answer.")
    print("1: Look up year range")
    print("2: Look up month/year")
    print("3: Search for author")
    print("4: Search for title")
    print("5: Number of authors with at least x bestsellers")
    print("6: List y authors with the most bestsellers")
    print("Q: Quit")

    answer=input("Please enter your answer: ")
    if answer=='1':
        yearrange(x)
    if answer=='2':
        monthyear(x)
    if answer=='3':
        author(x)
    if answer=='4':
        title(x)
    if answer=='5':
        frequency4(x)
    if answer=='Q'.lower():
        break
text.close()
    
