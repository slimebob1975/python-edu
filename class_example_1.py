class Person:
    """Klass för att hantera personuppgifter"""

    # Funktion som anropas när en klassinstans skapas
    def __init__(self, namn = "NN", instrument = "Inget", \
                 årsinkomst = 0 ):
        self.namn = namn                # Lägg till attribut namn
        self.instrument = instrument    # Lägg till attribut instrument
        self.årsinkomst = årsinkomst    # Lägg till attribut årsinkomst

    # Funktion som skriver ut dataattributen i formaterad form
    def skrivut(self):
        print("Person:\nNamn: {}\nInstrument: {}\nÅrsinkomst: {}" \
              .format(self.namn,self.instrument,self.årsinkomst))

    # Funktion som anropas när klassen skall skrivas ut med print
    def __str__(self):
        return self.namn+";"+self.instrument+";"+str(self.årsinkomst)

def main():
    person1 = Person("Nisse Landgren","Trombon",2000000)
    print(person1.__doc__)
    person1.skrivut()
    print(str(person1))
    print(person1)
    
main()
