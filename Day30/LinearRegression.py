def linearRegression(ArrPoints):
    xbar=ybar=xybar=xsqbar=0
    for i in ArrPoints:
        xbar+=i[0]
        ybar+=i[1]
        xybar+=i[0]*i[1]
        xsqbar+=i[0]**2
    xbar/=len(ArrPoints)
    ybar/=len(ArrPoints)
    xybar/=len(ArrPoints)
    xsqbar/=len(ArrPoints)
    print(xbar,ybar,xybar,xsqbar)
    a= ybar-(xybar-xbar*ybar)*xbar/(xsqbar-xbar**2)
    b= (xybar-xbar*ybar)/(xsqbar-xbar**2)
    print(a,b)


if __name__=='__main__':
    linearRegression([(-5,-10),(0,3),(2,11),(3,14)])