class perro:
    def __init__(self, hora):
        self.hora = hora

    # permite especificar tiempo en horas con numero entero
    def set_tomar_agua(self):

        for i in range(0, 5):
            if i == 4:
                self.hora = self.hora + 4

    # devuelve hora en que bebio agua
    def get_hora_toma_agua(self):
        return self.hora

    # indica si el perro necesita salir a caminar
    # true indica si el perro necesita salir a caminar
    # false
    def caminar(self, camina):
        if camina == 1:
            print("perro ya se encuentra caminando")
        else:
            self.set_tomar_agua
            self.get_hora_toma_agua
            print("perro debe caminar a la hora", self.hora)


# crear menu interaccion/ tiempo transcurrido para que sea sacado a pasear
# pedir la hora actual (?

hora = int(input("a que hora perro tomo agua?: "))
perro1 = perro(hora)
print("<1> a que hora debe caminar ")
print("<2> hora perro bebio agua")
opcion = int(input("opcion : "))
if opcion == 1:
    print("perro esta caminando?")
    print("<1> si ")
    print("<2> no")
    camina = int(input())
    perro1.caminar(camina)
if opcion == 2:
    print (perro1.get_hora_toma_agua(), "horas")

