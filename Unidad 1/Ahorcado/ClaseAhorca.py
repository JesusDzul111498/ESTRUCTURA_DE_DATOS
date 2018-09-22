import random
class entra:

    def buscar(self):
      palabras = ['progreso', 'valladolid', 'merida', 'buckzos', 'dzan', 'uyma',
          'tesoco', 'peto', 'rio', 'chelem', 'tizimin', 'xoquen', 'tekom ',
          'cuncunul','panaba', 'celestum', 'cuyo', 'cenotillo', 'seye', 'sucila',
          'tekax', 'tekit', 'popola', 'temozon','chemax', 'bokoba','izaml', 'ticul', ]

      palabraAadivinar = random.choice(palabras)
      return palabraAadivinar 

    def adivinar(self,palabra):
       np = " "
       inte = 10
       print("La palaba es: ")
       while inte > 0:
           error = 0
           for letra in palabra:
              if letra in np:
                   print(letra, end="")
              else:
                   print("_ ", end="")
                   error += 1
           if error == 0:
              print("\nHAS ADIVINADO FABULOSAMENTE LA PALABRA!!!")
              break

           tuletra = input("\nDIGITA TU LETRA: ")
           np += tuletra

           if tuletra not in palabra:
             inte -= 1
             print("intente de nuevo")
             print("tienes", +inte, "vidas")
           if inte == 0:
              print("\nNO HAS ADIVINADO LA PALABRA!!!")
       else:
               print("Gracias por jugar ")
               print("la palabra era: ",palabra)
