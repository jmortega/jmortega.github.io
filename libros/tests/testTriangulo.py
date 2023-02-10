"""
En este fichero se implementan los test para la clase Triangulo.
"""
import unittest
from src.Triangulo import Triangulo

class TestTriangulo(unittest.TestCase):
    """
    Esta clase implementa los test para la clase Triangulo.
    """
    def test_escaleno(self):
        """
        Test para el caso escaleno.
        """
        t = Triangulo()
        resultadoObtenido:str = t.tipoTriangulo(3, 4, 5)
        resultadoEsperado:str = "escaleno"
        self.assertEqual(resultadoEsperado, resultadoObtenido)

    def test_isosceles(self):
        """
        Test para el caso isosceles.
        """
        t = Triangulo()
        resultadoObtenido:str = t.tipoTriangulo(3, 3, 5)
        resultadoEsperado:str = "isósceles"
        self.assertEqual(resultadoEsperado, resultadoObtenido)
    
    def test_equilatero(self):
        """
        Test para el caso equilatero.
        """
        t = Triangulo()
        resultadoObtenido:str = t.tipoTriangulo(3, 3, 3)
        resultadoEsperado:str = "equilátero"
        self.assertEqual(resultadoEsperado, resultadoObtenido)
    
    def test_noTriangulo(self):
        """
        Test para el caso no triangulo.
        """
        t = Triangulo()
        resultadoObtenido:str = t.tipoTriangulo(3, 3, 6)
        resultadoEsperado:str = "no es un triángulo"
        self.assertEqual(resultadoEsperado, resultadoObtenido)
    
    def test_lado1FueraRango(self):
        """
        Test para el caso lado1 fuera de rango.
        """
        t = Triangulo()
        resultadoObtenido:str = t.tipoTriangulo(0, 3, 5)
        resultadoEsperado:str = "lado 1 fuera de rango"
        self.assertEqual(resultadoEsperado, resultadoObtenido)

    def test_lado2FueraRango(self):
        """
        Test para el caso lado2 fuera de rango.
        """
        t = Triangulo()
        resultadoObtenido:str = t.tipoTriangulo(3, 201, 5)
        resultadoEsperado:str = "lado 2 fuera de rango"
        self.assertEqual(resultadoEsperado, resultadoObtenido)

    def test_lado3FueraRango(self):
        """
        Test para el caso lado3 fuera de rango.
        """
        t = Triangulo()
        resultadoObtenido:str = t.tipoTriangulo(3, 3, 201)
        resultadoEsperado:str = "lado 3 fuera de rango"
        self.assertEqual(resultadoEsperado, resultadoObtenido)

if __name__ == '__main__':
    unittest.main()