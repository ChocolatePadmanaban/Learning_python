M3 = [list(range(5)) for i in range(6)]
for j in range(len(M3)-2):
    for i in range(len(M3[0])-2):
        X_i_j = [row[0+i:3+i] for row in M3[0+j:3+j]]
        print('=======')
        for x in X_i_j:
            print(x)