import json

class Calculator():
    def __init__(self):
        self.operand1=[]
        self.operand2=[]
        self.operation=[]
        self.result=[]

    def add(self,operand1,operand2):
        self.operand1=operand1
        self.operand2=operand2
        self.operation="Add"
        self.result=operand1+operand2
    def sub(self,operand1,operand2):
        self.operand1=operand1
        self.operand2=operand2
        self.operation="Subtraction"
        self.result=operand1-operand2
    def mul(self,operand1,operand2):
        self.operand1=operand1
        self.operand2=operand2
        self.operation="Multiplication"
        self.result=operand1*operand2
    def div(self,operand1,operand2):
        self.operand1=operand1
        self.operand2=operand2
        self.operation="Division"
        try:
            self.result=operand1/operand2
        except ZeroDivisionError:
            print("Errore divisione per zero\n")

a=Calculator()

while(1==1):
    string=input("Scrivi stringa\n")
    elements=string.split(" ")
    function=elements[0]
    operand1=float(elements[1])
    operand2=float(elements[2])

    if(function=='add'):
        a.add(operand1,operand2)
    elif(function=='sub'):
        a.sub(operand1,operand2)
    elif(function=='mul'):
        a.mul(operand1,operand2)
    elif(function=='div'):
        a.div(operand1,operand2)
    else:
        break
    dict={"Operand1": a.operand1, "Operand2": a.operand2, "Operation": a.operation, "Result": a.result}
    print(json.dumps(dict))