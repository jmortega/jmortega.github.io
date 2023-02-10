"""Implementación de la clase Triangulo"""

class Triangulo:
    """Esta clase representa un triángulo"""
    
    def tipoTriangulo(self, lado1:int, lado2:int, lado3:int) -> str:
        """
        Método que devuelve el tipo de triángulo.

        args:
            lado1: int
            lado2: int
            lado3: int

        returns:
            str: tipo de triángulo
        """
        if lado1 <= 1 or lado1 > 200:
            return "lado 1 fuera de rango"
        if lado2 <= 1 or lado2 > 200:
            return "lado 2 fuera de rango"
        if lado3 <= 1 or lado3 > 200:
            return "lado 3 fuera de rango"
        
        if lado1 + lado2 <= lado3:
            return "no es un triángulo"
        if lado1 + lado3 <= lado2:
            return "no es un triángulo"
        if lado2 + lado3 <= lado1:
            return "no es un triángulo"

        if lado1 == lado2 and lado2 == lado3:
            return "equilátero"
        elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
            return "isósceles"
        else:
            return "escaleno"

if __name__ == "__main__":
    print("Este módulo no se puede ejecutar directamente")