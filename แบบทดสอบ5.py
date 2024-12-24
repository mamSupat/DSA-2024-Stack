class Stack:
    def __init__(self):
        """สร้าง Stack เปล่า"""
        self.items = []

    def is_empty(self):
        """ตรวจสอบว่า Stack ว่างหรือไม่"""
        return len(self.items) == 0

    def push(self, item):
        """เพิ่มข้อมูลเข้า Stack"""
        self.items.append(item)

    def pop(self):
        """นำข้อมูลออกจาก Stack"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")

    def peek(self):
        """ดูข้อมูลที่อยู่บนสุดของ Stack"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")


def precedence(op):
    """
    กำหนดลำดับความสำคัญของตัวดำเนินการ
    """
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0


def apply_operator(operand1, operand2, operator):
    """
    คำนวณผลลัพธ์ของตัวดำเนินการและตัวถูกดำเนินการ 2 ตัว
    """
    if operator == '+':
        return operand1 + operand2
    if operator == '-':
        return operand1 - operand2
    if operator == '*':
        return operand1 * operand2
    if operator == '/':
        return operand1 / operand2
    if operator == '^':
        return operand1 ** operand2
    raise ValueError(f"ตัวดำเนินการไม่ถูกต้อง: {operator}")


def evaluate_infix(expression):
    """
    คำนวณผลลัพธ์ของ Infix Expression โดยใช้ Stack
    """
    operators = Stack()  # เก็บตัวดำเนินการ
    operands = Stack()   # เก็บตัวถูกดำเนินการ

    i = 0
    while i < len(expression):
        char = expression[i]

        # ข้ามช่องว่าง
        if char == ' ':
            i += 1
            continue

        # ถ้าเป็นตัวเลข (อาจเป็นหลายหลัก)
        if char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            operands.push(num)
            continue

        # ถ้าเป็นวงเล็บเปิด '('
        elif char == '(':
            operators.push(char)

        # ถ้าเป็นวงเล็บปิด ')'
        elif char == ')':
            while not operators.is_empty() and operators.peek() != '(':
                operator = operators.pop()
                operand2 = operands.pop()
                operand1 = operands.pop()
                operands.push(apply_operator(operand1, operand2, operator))
            operators.pop()  # เอาวงเล็บเปิด '(' ออกจาก Stack

        # ถ้าเป็นตัวดำเนินการ (+, -, *, /, ^)
        else:
            while (not operators.is_empty() and
                   precedence(operators.peek()) >= precedence(char)):
                operator = operators.pop()
                operand2 = operands.pop()
                operand1 = operands.pop()
                operands.push(apply_operator(operand1, operand2, operator))
            operators.push(char)

        i += 1

    # คำนวณตัวดำเนินการที่เหลือใน Stack
    while not operators.is_empty():
        operator = operators.pop()
        operand2 = operands.pop()
        operand1 = operands.pop()
        operands.push(apply_operator(operand1, operand2, operator))

    # ผลลัพธ์ที่เหลือใน Stack ตัวสุดท้ายคือคำตอบ
    return operands.pop()


# รับ Infix Expression จากผู้ใช้งาน
try:
    user_input = input("กรุณาป้อน Infix Expression (ตัวอย่าง: 3 + 5 * (2 - 8)): ")
    result = evaluate_infix(user_input)
    print(f"ผลลัพธ์: {result}")
except Exception as e:
    print(f"ข้อผิดพลาด: {e}")
