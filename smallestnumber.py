def smallest(li,n):
    for i in range(n):
        while(li[i]>=1 and li[i]<n and li[i]!=li[li[i]-1]):
            li[i],li[li[i]-1]=li[li[i]-1],li[i]   

        for i in range(n):
            if (li[i]!=i+1):
                return i+1

        return n+1

li= [int(ele) for ele in input("enter the element: ").split()] 
n=len(li)
print(smallest(li,n))


