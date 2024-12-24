class Stack:
    def __init__(self):
        """สร้าง Stack เปล่า"""
        self.items = []     # ใช้ list เก็บข้อมูลใน Stack
    
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
    
    def size(self):
        """ดูขนาดของ Stack"""
        return len(self.items)

# ทดสอบการทำงานของ Stack
def test_basic_operations():
    # สร้าง Stack ใหม่
    stack = Stack()
    
    # ทดสอบ push
    print("1. ทดสอบการ push ข้อมูล:")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack หลัง push: {stack.items}")
    
    # ทดสอบ peek
    print("\n2. ทดสอบการ peek:")
    print(f"ข้อมูลบนสุด: {stack.peek()}")
    
    # ทดสอบ pop
    print("\n3. ทดสอบการ pop:")
    print(f"ข้อมูลที่ pop: {stack.pop()}")
    print(f"Stack หลัง pop: {stack.items}")
    
    # ทดสอบ size
    print("\n4. ทดสอบการหาขนาด:")
    print(f"ขนาดของ Stack: {stack.size()}")

# เรียกฟังก์ชันทดสอบ
test_basic_operations()

# แบบฝึกหัด: การทดสอบ Stack เพิ่มเติม
print("\n--- แบบฝึกหัดเพิ่มเติม ---")
stack = Stack()

# 1. ทดสอบการ push ข้อมูล 5 ตัว
print("\n1. ทดสอบการ push ข้อมูล:")
for i in range(1, 6):
    stack.push(i)
    print(f"Push {i} -> Stack: {stack.items}")

# 2. แสดงข้อมูลบนสุดโดยใช้ peek
print("\n2. ทดสอบการ peek:")
print(f"ข้อมูลบนสุดใน Stack: {stack.peek()}")

# 3. ทดสอบ pop ข้อมูลออก 3 ตัว
print("\n3. ทดสอบการ pop ข้อมูลออก 3 ตัว:")
for _ in range(3):
    popped_item = stack.pop()
    print(f"Pop {popped_item} -> Stack: {stack.items}")

# 4. แสดงข้อมูลที่เหลือใน Stack
print("\n4. ข้อมูลที่เหลือใน Stack:")
print(f"Stack: {stack.items}")
