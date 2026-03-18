def devolver_distintos(n1, n2, n3):
    iter = [n1, n2, n3]
    total = sum(iter)
    if total > 15:
        return max(iter)
    elif total < 10:
        return min(iter)
    elif total >= 10 and total <= 15:
        return sorted(iter)[1] ## Solución no imaginada por mi, yo iba a sacar el max y el min y devolver el que quedaba.
    


def main():
    t1 = devolver_distintos(32, 1, 54)
    print(t1)
    
    t2 = devolver_distintos(1, 2, 3)
    print(t2)
    
    t3 = devolver_distintos(4, 5, 6)
    print(t3)

if __name__ == "__main__":
    main()