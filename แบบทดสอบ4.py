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


def is_json_valid(json_string):
    """
    ตรวจสอบความถูกต้องของ JSON string โดยใช้ Stack
    """
    stack = Stack()
    for char in json_string:
        if char in "{[":
            # เปิดวงเล็บเก็บเข้า Stack
            stack.push(char)
        elif char in "]}":
            # ปิดวงเล็บตรวจสอบว่าตรงกับตัวเปิดใน Stack หรือไม่
            if stack.is_empty():
                return False
            top = stack.pop()
            if char == "}" and top != "{":
                return False
            if char == "]" and top != "[":
                return False
    
    # ถ้า Stack ว่างแสดงว่าวงเล็บถูกต้อง
    return stack.is_empty()


# รับ JSON string จากผู้ใช้งาน
try:
    user_input = input("กรุณาป้อน JSON string ที่ต้องการตรวจสอบ: ")
    if is_json_valid(user_input):
        print("JSON string ถูกต้อง")
    else:
        print("JSON string ไม่ถูกต้อง")
except Exception as e:
    print(f"ข้อผิดพลาด: {e}")
