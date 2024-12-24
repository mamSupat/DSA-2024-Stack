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


# ฟังก์ชันสำหรับคำนวณ Postfix Expression
def evaluate_postfix(expression):
    """
    คำนวณผลลัพธ์ของนิพจน์ในรูปแบบ Postfix
    - expression: นิพจน์ Postfix (แยกค่าด้วยช่องว่าง เช่น "3 4 + 2 *")
    """
    stack = Stack()
    tokens = expression.split()  # แยกนิพจน์ออกเป็นแต่ละส่วน

    for token in tokens:
        if token.isdigit():  # ถ้าเป็นตัวเลข
            stack.push(int(token))
        elif token in "+-*/":  # ถ้าเป็นตัวดำเนินการ
            # นำตัวเลขสองตัวบนสุดใน Stack ออกมาเพื่อดำเนินการ
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("ไม่สามารถหารด้วยศูนย์ได้")
                stack.push(a / b)
        else:
            raise ValueError(f"พบตัวอักษรที่ไม่สามารถประมวลผลได้: {token}")

    # ผลลัพธ์สุดท้ายควรเหลืออยู่ใน Stack เพียงตัวเดียว
    if stack.is_empty():
        raise ValueError("นิพจน์ไม่ถูกต้อง")
    
    return stack.pop()


# รับนิพจน์ Postfix จากผู้ใช้งาน
try:
    user_input = input("กรุณาป้อนนิพจน์ Postfix (แยกด้วยช่องว่าง เช่น '3 4 + 2 *'): ")
    result = evaluate_postfix(user_input)
    print(f"ผลลัพธ์ของนิพจน์: {result}")

except (ValueError, ZeroDivisionError, IndexError) as e:
    print(f"ข้อผิดพลาด: {e}")
