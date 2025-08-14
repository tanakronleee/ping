#ปี 1 เทอม 1 ตรวจสอบความปลอดภัยรหัสอย่างง่าย
password = input("กรุณาป้อนรหัสผ่านเพื่อตรวจสอบ: ")
print(f"กำลังตรวจสอบรหัสผ่าน: {password}")
import string # Library ที่ช่วยให้เราเข้าถึงชุดอักขระต่างๆ ได้ง่าย

def check_password_strength(password): #ฟังก์ชันตรวจสอบความแข็งแรงของรหัสผ่าน
    score = 0
    if len(password) < 8:
        print("รหัสผ่านต้องมีความยาว 8 ตัวอักษรขี้นไป")
        score += 1
    if not any(char.isupper() for char in password): #เช็คว่ามีตัวอักษรพิมพ์ใหญ่ในรหัสผ่าน
        print("รหัสผ่านต้องมีตัวอักษรพิมพ์ใหญ่")
        score += 1
    if not any(char.islower() for char in password): #เช็คว่ามีตัวอักษรพิมพ์เล็กในรหัสผ่าน
        print("รหัสผ่านต้องมีตัวอักษรพิมพ์เล็ก")
        score += 1
    if not any(char.isdigit() for char in password): #เช็คว่ามีตัวเลขในรหัสผ่าน
        print("รหัสผ่านต้องมีตัวเลข")
        score += 1
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?`~"
    if any(char in special_characters for char in password):
        score += 1

    return score

def main():
    """
    ฟังก์ชันหลักของโปรแกรม
    """
    score = check_password_strength(password)
    
    print("\n--- ผลการตรวจสอบ ---")
    print(f"คะแนนความแข็งแกร่ง: {score}/5")

    if score <= 2:
        print("ระดับ: 😥 อ่อน (Weak)")
        print("คำแนะนำ: ควรมีความยาวอย่างน้อย 8 ตัวอักษร และผสมตัวอักษรใหญ่, เล็ก, ตัวเลข, และอักขระพิเศษ")
    elif score == 3:
        print("ระดับ: 🤔 ปานกลาง (Medium)")
        print("คำแนะนำ: ลองเพิ่มอักขระพิเศษ หรือเพิ่มความยาวเพื่อให้แข็งแกร่งขึ้น")
    elif score == 4:
        print("ระดับ: 👍 แข็งแกร่ง (Strong)")
        print("คำแนะนำ: รหัสผ่านของคุณดีแล้ว! อาจเพิ่มความยาวเพื่อความปลอดภัยสูงสุด")
    else: # score == 5
        print("ระดับ: 🚀 แข็งแกร่งมาก (Very Strong)")
        print("สุดยอด! รหัสผ่านของคุณปลอดภัยมาก")
    print("ขอบคุณที่ใช้โปรแกรมตรวจสอบความแข็งแรงของรหัสผ่าน")
# สั่งให้โปรแกรมเริ่มทำงานที่ฟังก์ชัน main เมื่อไฟล์นี้ถูกรันโดยตรง
if __name__ == "__main__":

    main()
