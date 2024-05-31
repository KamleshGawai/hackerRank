
n = int(input())
total=0
if (n>=2)and(n<=10):
    
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for i in student_marks:
        if i==query_name:
            for j in range(3):
                
                total=total+student_marks[i][j]


    avrage_score=total/3


print(f'{avrage_score:.2f}')
