import sys
def simInt(principal,interest,time):
    return(principal* interest*time)/100
if __name__ == "__main__":
    p=int(sys.argv[1])
    i=int(sys.arvg[2])
    t=int(sys.arvg[3])

    print("Simple interest:",simInt(p,i,t))