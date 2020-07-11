def gcd(m,n):
    if m<n:
        (m,n) = (n,m)
    while (m%n) !=0:
        diff = m - n
        (m,n) = (max(n,diff),min(n,diff))

        return(n)


    #even better

    def gcd(m,n):
        if m <n:
            (m,n) = (n,m)

        if (m%n) == 0:
            return(n)
        else:
            return(gcd(n,m%n)) #where m%n is remainder ie. r

