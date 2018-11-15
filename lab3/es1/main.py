import requests
import json
while True:
    a=input("Give me the first operand\n")
    b=input("Give me the second operand\n")
    c=input("Operation needed to do with the two operands\n")

    if a=="quit" or b=="quit" or c=="quit":
        print("Quitting program....")
        break

    operand1=float(a)
    operand2=float(b)

    if c=='addiction':
        result=requests.get("http://localhost:9090/add"+"?&op1="+a+"&op2="+b).json()
        #json_data=json.loads(result)
    elif c=='subtraction':
        result=requests.get("http://localhost:9090/sub"+"?&op1="+a+"&op2="+b).json()
        #json_data=json.loads(result)
    elif c=='multiplication':
        result=requests.get("http://localhost:9090/mul"+"?&op1="+a+"&op2="+b).json()
        #json_data=json.loads(result)
    elif c=='division':
        result=requests.get("http://localhost:9090/div"+"?&op1="+a+"&op2="+b).json()
        #json_data=json.loads(result)


    print("Operand 1 = ", result["operand1"])
    print("Operand 2 = ", result["operand2"])
    print("Result = ", result["result"])

