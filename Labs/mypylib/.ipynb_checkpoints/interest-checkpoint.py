def main():
    print("hello world")

def amount(A0, p, n):
    '''This is a thing'''
    A = A0*(1+(p/(360*100)))**n
    return A
def p_inter(A, A0, n):
    p = ((A/A0)**(1/n)-1)*360*100
    return p