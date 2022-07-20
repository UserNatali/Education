import math
input("\n\t1. Додавання \n\t2. Віднімання \n\t3. Множення \n\t4. Ділення \n\t5. Піднесення до степеня \n\t6. sin x"
      " \n\t7. cos x \n\t8. tg x")
choice = int(input("Select a operation :"))

match choice:
      case 1:
            number1 = float(input("Input first number: "))
            number2 = float(input("Input second number: "))
            sum = number1 + number2
            print(sum)
      case 2:
            number1 = float(input("Input first number: "))
            number2 = float(input("Input second number: "))
            difference = number1 - number2
            print(difference)
      case 3:
            number1 = float(input("Input first number: "))
            number2 = float(input("Input second number: "))
            product = round(number1 * number2)
            print(product)
      case 4:
            number1 = float(input("Input first number: "))
            number2 = float(input("Input second number: "))
            if number2 != 0:
                  quotient = number1 / number2
                  print(quotient)
            else:
                  print("Cannot be divided by zero")
      case 5:
            number1 = float(input("Input first number: "))
            number2 = float(input("Input second number: "))
            quotient = number1 ** number2
            print(quotient)
      case 6:
            angle_degree = float(input("Input angle degree: "))
            sin = round(math.sin(angle_degree), 3)
            print(sin)
      case 7:
            angle_degree = float(input("Input angle degree: "))
            cos = round(math.cos(angle_degree), 3)
            print(cos)
      case 8:
            angle_degree = float(input("Input angle degree: "))
            tg = round(math.tan(angle_degree), 3)
            print(tg)
      case _:
            print("wrong choice")

