#Get the next next IP Address 


def NextIP(a, increment):
    if a < 255:
        return 0, a+increment
    else:
        return 1, 0
def NextIPAddress(a):
    a = a.split('.')
    a = [int(i) for i in a]
    increment = 1
    for i in range(3,-1,-1):
        increment , a[i] = NextIP(a[i], increment)
    return ".".join([str(i) for i in a])

print(NextIPAddress("192.233.255.255"))



