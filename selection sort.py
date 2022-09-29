'''selection sort'''
a=[5,4,3,2,1]
for i in range (len(a)):
    for j in range (i+1,len(a)):
        if(a[i]>a[j]):
            tem=a[i]
            a[i]=a[j]
            a[j]=tem
   
for i in range(len(a)):
    print(a[i])
    