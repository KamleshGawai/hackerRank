x=1
y=1
z=1

n=3

list1=[]

for i in range(0,x+1,1):
    for j in range(0,y+1,1):
        for k in range (0,z+1,1):
            li=[i,j,k]
            l=i+j+k
            if l!=n:

                list1.append(li)


print(list1)                
                
            
