## 对一个数组，实现将其前K个大数替换为1，其余替换0为0
def qselect(A,k):
  if len(A)<k:return A
  pivot = A[-1]
  right = [pivot] + [x for x in A[:-1] if x>=pivot]
  rlen = len(right)
  if rlen==k:
    return right
  if rlen>k:
    return qselect(right, k)
  else:
    left = [x for x in A[:-1] if x<pivot]
    return qselect(left, k-rlen) + right

##排序，返回有前K个大数的数组

def predict_seq1(a,b):
    c=[]
    for x in a:
        for y in b:
            x=1 if x==y else x
        c.append(x)
    return c

###返回前K个大数替换为1的数组

def predict_seq2(a):
    c=[]
    for x in a:
        x=0 if x!=1 else x
        c.append(x)
    return c

### 将数组中不为0的元素替换为0
a=[18,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(qselect(a,10))##[9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
b=qselect(a,10)
print(predict_seq1(a,b))##[1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1]
c=predict_seq1(a,b)
print(predict_seq2(c))##[1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
