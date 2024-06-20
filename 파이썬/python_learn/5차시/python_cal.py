for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if 9*i*k+j*k-10*i*j==0:
                print(i,j,k)