def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b

def main():
    print("간단한 계산기")
    print("작업: +, -, *, /")
    a = float(input("첫 번째 숫자: "))
    op = input("연산자: ").strip()
    b = float(input("두 번째 숫자: "))

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = subtract(a, b)
    elif op == "*":
        result = multiply(a, b)
    elif op == "/":
        result = divide(a, b)
    else:
        print("유효하지 않은 연산자입니다.")
        return

    print(f"결과: {result}")

if __name__ == "__main__":
    main()