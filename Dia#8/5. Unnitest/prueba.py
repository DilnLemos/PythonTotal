import unittest
import cambia_texto

class Prueba_Cambia_Texto(unittest.TestCase):
    
    def test_mayusculas(self):
        palabra = "buen día"
        resultado = cambia_texto.todo_mayusuculas(palabra)
        
        self.assertEqual(resultado, "BUEN DÍA")
        
if __name__ == '__main__':
    unittest.main()