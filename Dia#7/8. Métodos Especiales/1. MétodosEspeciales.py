mi_lista = [1,2,3,4]
print(len(mi_lista))

"----------------------"

class Libro:
    def __init__(self, autor, titulo, cant_paginas):
        self.autor = autor
        self.titulo = titulo
        self.cant_paginas = cant_paginas
        
    def __str__(self):
        return f'Título: "{self.titulo}", escrito por {self.autor}'
    
    def __len__(self):
        return self.cant_paginas
    
    def __del__(self):
        print("Libro eliminado")

libro1 = Libro("Stephen King", "It", 1032)
print(str(libro1))
print(len(libro1))
del libro1