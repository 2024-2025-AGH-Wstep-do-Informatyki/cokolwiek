import calculate
import onp
import sysConv

class interface:
    def __init__(self):
        print("Witaj w Inteligentnym Modularnym Kalkulatorze")
        self.showModules()

    def showModules(self):
        self.showHelp()

        while(True):
            wybor = input("Wprowadź wybór: ")
            match(wybor.upper()):
                case "A":
                    self.standardCalc()
                case "B":
                    self.convertNumberSystem()
                case "Q":
                    self.quitCalc()
                case "HELP":
                    self.showHelp()
                case _:
                    print("Wprowadzony ciąg nie pasuje do żadnego dostepnego modułu. Spróbuj ponownie")

    def standardCalc(self):
        expression = self.inputExpression()
        print("Wynikiem " + expression + " jest: ")
        print(calculate.calc(onp.onp(expression)))

    def convertNumberSystem(self):
        number = self.intInput("Wprowadź liczbę którą chcesz przekonwertować (int): ")
        st = self.intInput("Wprowadź system z którego chcesz przekonwertować liczbę (int): ")
        fin = self.intInput("Wprowadź system na który chcesz przekonwertować liczbę (int): ")
        print(sysConv.convSys(st,fin,number))


    def quitCalc(self):
        quit()

    def showHelp(self):
        print("Obecnie dostępne są poniższe moduły (wpisz literę aby wybrać)")
        print("A - Standardowy Kalkulator")
        print("B - Zamiana systemów liczbowych")
        print("Q - Wyjdź z programu")

    def inputExpression(self):
        while True:
            expression = input("Wprowadź działanie które chcesz rozwiązać: ")
            if onp.onp(expression):
                return expression
            print("Nieprawidłowe działanie, spróbuj ponownie")

    def intInput(self, message) -> int:
        while True:
            try:
                num = int(input(message))
                break
            except ValueError:
                print("Nieprawidłowy input, podaj poprawną liczbę całkowitą")
        return num

interf = interface()