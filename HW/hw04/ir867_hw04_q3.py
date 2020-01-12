#hw 4
#ir867

def print_triangle(n):
    if n<=0:
        return
    else:
        print_triangle(n-1)
        print(n*"*")

def print_opposite_triangle(n):
    if n<=0:
        return
    else:
        print(n*"*")
        print_opposite_triangle(n-1)
        print(n*"*")
    

def print_ruler(n):
    if(n==0):
        return
    print_ruler(n-1)
    print("-"*n)
    print_ruler(n-1)

