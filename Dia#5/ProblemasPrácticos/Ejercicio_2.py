
def devolver_string(string):
    string = set(string)
    string = sorted(string) # Ordena caracteres alfabéticamente por codigo ASCII
    return string

def main():
    result = devolver_string("Hola, mundo!")
    print(result)

if __name__ == "__main__":
    main()