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

# ฟังก์ชันกลับลำดับตัวอักษรโดยใช้ Stack
def reverse_string_with_stack(input_string):
    stack = Stack()
    
    # เพิ่มตัวอักษรแต่ละตัวลงใน Stack
    for char in input_string:
        stack.push(char)
    
    # นำตัวอักษรออกจาก Stack และสร้างข้อความใหม่ (ย้อนกลับลำดับ)
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# รับข้อความจากผู้ใช้งาน
user_input = input("กรุณาป้อนข้อความที่ต้องการกลับลำดับตัวอักษร: ")
result = reverse_string_with_stack(user_input)

# แสดงผลลัพธ์
print(f"ข้อความที่กลับลำดับ: {result}")
