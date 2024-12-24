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

    def size(self):
        """ดูขนาดของ Stack"""
        return len(self.items)


# ฟังก์ชันแปลงเลขฐาน 10 เป็นเลขฐานอื่นโดยใช้ Stack
def convert_base(decimal_number, base):
    """
    แปลงเลขฐาน 10 เป็นเลขฐานที่ต้องการ (2 หรือ 16)
    - decimal_number: ตัวเลขฐาน 10 ที่ต้องการแปลง
    - base: เลขฐานเป้าหมาย (2 หรือ 16)
    """
    if base not in [2, 16]:
        raise ValueError("รองรับเฉพาะการแปลงเป็นฐาน 2 หรือฐาน 16 เท่านั้น")

    # ตัวเลขและตัวอักษรที่ใช้ในเลขฐาน 16
    digits = "0123456789ABCDEF"
    stack = Stack()

    # แปลงเลขฐาน 10 เป็นฐานที่ต้องการ
    while decimal_number > 0:
        remainder = decimal_number % base
        stack.push(digits[remainder])
        decimal_number //= base

    # ดึงตัวเลขออกจาก Stack เพื่อสร้างผลลัพธ์
    result = ""
    while not stack.is_empty():
        result += stack.pop()

    return result


# รับตัวเลขฐาน 10 จากผู้ใช้งาน
try:
    decimal_number = int(input("กรุณาป้อนตัวเลขฐาน 10 ที่ต้องการแปลง: "))

    # แปลงเป็นฐาน 2 (Binary)
    binary_result = convert_base(decimal_number, 2)
    print(f"เลขฐาน 2 ของ {decimal_number}: {binary_result}")

    # แปลงเป็นฐาน 16 (Hexadecimal)
    hexadecimal_result = convert_base(decimal_number, 16)
    print(f"เลขฐาน 16 ของ {decimal_number}: {hexadecimal_result}")

except ValueError:
    print("กรุณาป้อนตัวเลขฐาน 10 ที่ถูกต้อง")
