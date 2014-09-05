# coding=utf-8
#
#  anivemin.py
#
#  2014 by carxofeta.
#
import string


class Elemento:
    """Creo una clase Elemento, con un puntero a otro Elemento a izquierda y derecha"""
    def __init__(self, pregunta, left=None, right=None):
        self.pregunta = pregunta
        self.left = left
        self.right = right


def respuesta(respuesta):
    """El usuario responde si o no. Obviamente, S� devuelve True"""
    while 1:
        res = raw_input(respuesta)
        res = string.lower(res[0:1])
        if res == 's':
            return 1
        else:
            return 0

conoce = Elemento("p�jaro")


def main():
    """Trata de adivinar el animal. A�adimos un nuevo Elemento en caso de no adivinarlo."""
    while 1:
        print
        if not respuesta("Est�s pensando en un animal? "):
            break
        p = conoce
        while p.left is not None:
            if respuesta(p.pregunta + "? "):
                p = p.right
            else:
                p = p.left

        if respuesta("Es un " + p.pregunta + "? "):
            print "�Biennnn! Lo adivin�, �soy un crack!"
            continue
        animal = raw_input("�Cu�l es el nombre del animal que pensabas? ")
        question = raw_input("�Qu� frase distinguir�a a %s de un %s? " % (animal, p.pregunta))
        p.left = Elemento(p.pregunta)
        p.right = Elemento(animal)
        p.pregunta = question

        if not respuesta("Si el animal fuese un %s la respuesta ser�a... " % animal):
            (p.right, p.left) = (p.left, p.right)

if __name__ == "__main__" : main()

