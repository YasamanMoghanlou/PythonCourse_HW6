def honai(n, A, B, C):
    if n == 1 :
        print ("move ring 1 from", A, "to", B)
        return
    honai (n-1, A, C, B)
    print ("move ring", n, "from", A, "to", B)
    honai(n-1, C, B, A)
    
num = int (input("enter number of rings: "))
honai (num, "A", "B", "C")