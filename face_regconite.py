import cv2

cam = cv2.VideoCapture(0)

print("กด 'q' เพื่อปิดหน้าต่าง")

while True:
    ret, frame = cam.read()
    if not ret:
        print("ไม่สามารถอ่านข้อมูลจากกล้องได้")
        break

    # แสดงผลภาพจากกล้อง
    cv2.imshow("กล้อง", frame)

    # ตรวจสอบการกดปุ่ม 'q' เพื่อหยุดโปรแกรม
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("ปิดกล้อง")
        break

cam.release()
cv2.destroyAllWindows()
