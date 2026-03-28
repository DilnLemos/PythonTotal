class Crossfitero:
    
    atleta = True # Atributo de clase
    
    def __init__(self, nombre, edad):
        self.nombre = nombre # Atributo de instancia
        self.edad = edad # Atributo de instancia
    
    def entrenar(self):
        print(f"{self.nombre} está entrenando, que hpta máquina.")
        
    def snatch(self, peso):
        print(f"{self.nombre} está haciendo RM en snatch con {peso} kg.")
        
    def clean_and_jerk(self, peso):
        print(f"{self.nombre} está haciendo RM en clean and jerk con {peso} kg.")
        
    def squat_clean(self, peso):
        print(f"{self.nombre} está haciendo RM en squat clean con {peso} kg.")
        
    

Dilnlemos = Crossfitero("Dilnlemos", 19)
Dilnlemos.entrenar()
Dilnlemos.snatch(50)
Dilnlemos.clean_and_jerk(65)
Dilnlemos.squat_clean(80)
