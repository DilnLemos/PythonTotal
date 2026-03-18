
def ceros_consecutivos(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False

def main():
    print(ceros_consecutivos(1, 2, 0, 0, 3, 4))  # True
    print(ceros_consecutivos(1, 2, 0, 3, 4))     # False

if __name__ == "__main__":
    main()