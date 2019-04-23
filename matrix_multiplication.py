print"enter the elements of matrix in the form of \n[[x11,x12,.....,x1n],[x21,x22,...x2n],...,[xm1,xm2,...xmn]"
x=input("enter the elements of matrix1:")
y=input("enter the elements of matrix2:")
a=len(x)
b=len(x[0])
c=len(y)
d=len(y[0])
mat=[]
for i in range(a):
	if(b!=c):
		print("multiplication of given two matrices is not possible")
	m1=[]
	for j in range(d):
		sum=0
		for k in range(c):
			sum=sum+(x[i][k]*y[k][j])
		m1.append(sum)
	mat.append(m1)
print mat
print
