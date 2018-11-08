import json


class Calculator():
    def __init__(self):
        self.operand = []
        self.result = []

    def add(self, operand):
        self.operand = operand
        self.operation = "Add"
        result = 0
        for i in range(len(operand)):
            result += operand[i]
        self.result = result

    def sub(self, operand):
        self.operand = operand
        self.operation = "Subtraction"
        result = operand[0]
        for i in range(1, len(operand)):
            result -= operand[i]
        self.result = result

    def mul(self, operand):
        self.operand = operand
        self.operation = "Multiplication"
        result = operand[0]
        for i in range(1, len(operand)):
            result *= operand[i]
        self.result = result

    def div(self, operand):
        self.operand = operand
        self.operation = "Division"
        result=operand[0]
        for i in range(1,len(operand)):
            try:
                result /= operand[i]
            except ZeroDivisionError:
                print("Errore divisione per zero\n")
                return
        self.result=result



a = Calculator()

while (1 == 1):
    string = input("Scrivi stringa\n")
    elements = string.split(" ")
    operand = []
    function = elements[0]
    for i in range(1, len(elements)):
        operand.append(float(elements[i]))

    if (function == 'add'):
        a.add(operand)
    elif (function == 'sub'):
        a.sub(operand)
    elif (function == 'mul'):
        a.mul(operand)
    elif (function == 'div'):
        a.div(operand)
    else:
        break
    dict = [{"Operand": a.operand, "Operation": a.operation, "Result": a.result}]
    print(json.dumps(dict))
