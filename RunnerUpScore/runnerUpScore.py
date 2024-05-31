
n = int(input())
if n >= 2 and n<= 10:
    
    arr=input().split()
    arr1=[]
    k=0

    arr1 = [eval(i) for i in arr]

    arr1.sort()



    a=int(max(arr1))

    for i in range(a,-100,-1):

        if k==0:
            for j in range(len(arr1)):

                if i-1==arr1[j]:
                    k=1
                    print(arr1[j])
                    break
        else:
            break
    
        
    
