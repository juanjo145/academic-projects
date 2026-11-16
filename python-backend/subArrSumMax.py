
def phi(A):
    ans,psum,N  = 0,0,len(A)

    for n in range(N):
        psum = max(psum+A[n],A[n])
        ans = max(ans,psum)
    return(ans)
A =[2,-1,4,-2,0,3,6,-2]
print(phi(A))
    