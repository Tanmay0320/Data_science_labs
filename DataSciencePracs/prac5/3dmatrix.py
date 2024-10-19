rows = 7   
cols = 5
depth = 3      

matrix = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(depth)]
    
def update_matrix(matrix):
    for d in range(depth):
        for r in range(rows):
            for c in range(cols):
                index_sum = d + r + c
                if index_sum % 2 == 0:
                    matrix[d][r][c] = 0
                else:
                    matrix[d][r][c] = 1

    return matrix
    
def findit(matrix):
    count=0
    largest1=0
    largest2=0
    largest3=0
    list1=[]
    list11=[]
    list2=[]
    list22=[]
    list3=[]
    list33=[]
    for d in range(depth):
        for r in range(rows):
            for c in range(cols):
                if matrix[d][r][c] == 1:
                    count+=1
                    list1.append([r,c,d])
                else:
                    largest1=count
                    list11=list1.copy()
                    list1.clear()
                    count=0
                if(c==cols-1):
                    largest1=count
                    list11=list1.copy()
                    list1.clear()
                    count=0
    count=0              
    for d in range(depth):
        for c in range(cols):
            for r in range(rows):
                if matrix[d][r][c] == 1:
                    count+=1
                    list2.append([r,c,d])
                else:
                    largest2=count
                    list22=list2.copy()
                    list2.clear()
                    count=0
                if(r==rows-1):
                    largest1=count
                    list11=list1.copy()
                    list1.clear()
                    count=0
    count=0              
    for r in range(rows):
        for c in range(cols):
            for d in range(depth):
                if matrix[d][r][c] == 1:
                    count+=1
                    list3.append([r,c,d])
                else:
                    largest3=count
                    list33=list3.copy()
                    list3.clear()
                    count=0
                if(d==depth-1):
                    largest1=count
                    list11=list1.copy()
                    list1.clear()
                    count=0
                    
    if(largest1>largest2):
        if(largest1>largest3):
            print("length of the largest sub string of one:"+str(largest1))
            print("coords of the largest sub string of one=")
            print(list11)
        else:
            print("length of the largest sub string of one:"+str(largest3))
            print("coords of the largest sub string of one=")
            print(list33)
    elif(largest2>largest3):
        print("length of the largest sub string of one:"+str(largest2))
        print("coords of the largest sub string of one=")
        print(list22)
    else:
        print("length of the largest sub string of one:"+str(largest3))
        print("coords of the largest sub string of one=")
        print(list33)
        
updated_matrix = update_matrix(matrix)

for d in updated_matrix:
    for r in d:
        print(r)
    print("-----")
    
findit(updated_matrix)