

def main():
    tmp = sum([i*i for i in range(1,11)])
    print("Az első tíz természetes szám négyzetösszege: "+str(tmp))
    tmp = sum(range(1,11))**2
    print("Az első tíz természetes szám összegének a négyzete: "+str(tmp))

if __name__=="__main__":
    main()