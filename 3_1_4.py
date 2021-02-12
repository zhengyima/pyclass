def hannoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        hannoi(n-1, x, z, y)
        print(x,'-->',z)
        hannoi(n-1, y, x, z)
 
n=int(input("请输入x,yz："))   
hannoi(n, "X", "Y", "Z")