import csv
import numpy as np

# read data in Ground truth file and return a single vector containing s1,s2,s3...
def Read_GT(file_name):
    data = []
    with open(file_name, newline='\n') as csvfile:
        x = csv.reader(csvfile, delimiter=',')
        for rows in x :
            for i in rows :
                data.append(float(i))
    return data

# read data file and return a data object contains of rows * columns
def read_data(file_name):
    data = []
    with open(file_name, newline='\n') as csvfile:
        x = csv.reader(csvfile, delimiter=',')
        for rows in x :
            for i in range(len(rows)):
                rows[i] = float(rows[i])
            data.append(rows)
        
    return data

# read file and return a data object with the same size of (3 * row lenght) * 12 
def Read_File(file_name):
    M = []
    j=0
    with open(file_name, newline='\n') as csvfile:
        x = csv.reader(csvfile, delimiter=',')
        for rows in x :
            M.extend(build_m(rows))
    return M

# building a 3 * 12 matrix from a row that had been read from the file
def build_m(row):
    m = []
    row1=[]
    row2=[]
    row3=[]
    zeros=[0,0,0,0]
    for i in range(len(row)):
        row[i] = float(row[i])
    row.append(1)
    for i in range(3):
        if i == 0:
            row1.append(row)
            row1.append(zeros)
            row1.append(zeros)
            row1 = sum(row1,[])
        elif i == 1:
            row2.append(zeros)
            row2.append(row)
            row2.append(zeros)
            row2 = sum(row2,[])
        elif i == 2:
            row3.append(zeros)
            row3.append(zeros)
            row3.append(row)
            row3 = sum(row3,[])
    m.append(row1)
    m.append(row2)
    m.append(row3)
    # for i in range(len(m)):
    #     for j in range(len(m[i])):
    #         print(m[i][j],end=' ')
    #     print()
    # print(row3)
    return m

def create_A_b(B):
    A = (B[0:3],B[4:7],B[8:11])
    A = np.array(A)
    b = [B[3],B[7],B[11]]
    b = np.array(b)
    return A,b


Grd_truth = Read_GT("groundtruth.csv")
measurements = Read_File("measurements.csv")

# B = (Mt * M)-1 * M * sigma

# print(measurements)
M = np.array(measurements)
# print(M.shape)
Mt = M.transpose()
# print(Mt.shape)
temp = Mt.dot(M)
# print(temp.shape)
temp2 = np.linalg.pinv(temp)
# print(temp2.shape)
temp3 = temp2.dot(M.transpose())
sigma = np.array(Grd_truth)
# print(sigma.shape)
B = temp3.dot(sigma)

B = B.tolist()
# print(B)
A,b = create_A_b(B)
# print(A)
# print(b)

r = read_data("measurements.csv")
r = np.array(r)
# print(r.shape)

# applying a correction function on the data read from the measurment.csv ( y = A*r + b)
for i in range(r.shape[0]):
    # print(r[i].shape)
    r[i] = A.dot(r[i]) + b

# print(r.shape)
Grd_truth = read_data("groundtruth.csv")
Gth = np.array(Grd_truth)
# print(Gth.shape)

# computing the sum of squares error
sum =0
for i in range(r.shape[0]):
    for j in range(3):
        if i == 0:
            sum += (Gth[i][j] - r[i][j])**2

print(sum)