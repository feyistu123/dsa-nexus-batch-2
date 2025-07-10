if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
  
    scores = []
    for record in records:
        scores.append(record[1])
   
    scores = list(set(scores))
    sorted_scor = sorted(scores)
    
    sec_low = sorted_scor[1]
    sec_low_students=[]
    for student in records:
        if student[1] == sec_low:
            sec_low_students.append(student[0])
    sec_low_students.sort()
    for name in sec_low_students:
        print(name)  
            
