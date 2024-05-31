n=int(input())
trigger=0
name=[]
score=[]
secLow=0
data=[[],[],[],[],[]]
name1=[]
for i in range(n):
    if n<=5:
        
        name.append(input())
        score.append(float(input()))



for i in range(0,n,1):
    
    for j in range(0,1,1):
        data[i].append(i)
        data[i].append(name[i])
        data[i].append(score[i])
        

minno=min(score)


for i in range(n):
    for j in range(0, n - i - 1):
            
        if score[j] > score[j + 1]:
            score[j], score[j + 1] = score[j + 1], score[j]
                

for i in range(len(score)):
    
    if trigger == 0:
        
        
        for j in range(1,len(score),1):
            if score[j]==minno:
                continue
            else:
                secLow=score[j]
                
                trigger=1
                break
    else:
        break
    
for i in range(n):
    if data[i][2]==secLow:
        
        name1.append(data[i][1])


name1.sort()

for i in name1:
    print(i)
