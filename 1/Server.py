import socket
import threading

# قائمة الأسئلة
QUESTIONS = [
    "What is the result of 5 + 3?",
    "What is the result of 7 - 2?",
    "What is the result of 4 * 6?",
    "What is the result of 10 / 2?",
    "What is the result of 9 % 4?",
    "What is the square root of 25?",
    "What is the cube root of 27?",
    "What is the result of (2 + 3) * 4?",
    "What is the result of 2^3?",
    "What is the result of (6 * 4) / (2 + 1)?"
]

# قائمة الإجابات الصحيحة
ANSWERS = [
    "8",
    "5",
    "24",
    "5",
    "1",
    "5",
    "3",
    "20",
    "8",
    "8"
]

# تابع لمعالجة اتصال العميل
def handle_client(csock, caddr):
    # متغير لتخزين عدد الإجابات الصحيحة
    a = 0
    # حلقة لإرسال الأسئلة وتلقي الإجابات
    for i in range(len(QUESTIONS)):
        # إرسال السؤال إلى العميل
        csock.sendall(QUESTIONS[i].encode())
        # تلقي الإجابة من العميل وإزالة الأحرف الفارغة
        answer = csock.recv(1024).decode().strip()
        # التحقق من صحة الإجابة وزيادة العدد في حالة الصحة
        if answer == ANSWERS[i]:
            a += 1
    # إرسال عدد الإجابات الصحيحة إلى العميل
    csock.sendall(f"Your final result is {a}".encode())
    # إغلاق الاتصال
    csock.close()
    # طباعة رسالة للتحقق من إغلاق الاتصال
    print(caddr, "closed connection")

# تابع لبدء السيرفر
def start_server(host, port):
    # إنشاء socket وربطه بالمضيف والمنفذ
    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ssock.bind((host, port))
    # الاستماع على الاتصالات الواردة
    ssock.listen()
    # طباعة رسالة للتحقق من بدء السيرفر
    print(f"Server listening on {host}:{port}")
    # حلقة لقبول الاتصالات الجديدة
    while True:
        # قبول الاتصال وإنشاء socket جديد لكل عميل
        csock, caddr = ssock.accept()
        # طباعة رسالة للتحقق من قبول الاتصال
        print(f"Accepted connection from {caddr[0]}:{caddr[1]}")
        # إنشاء thread جديد لكل عميل وتشغيله على التابع handle_client()
        threading.Thread(target=handle_client, args=(csock, caddr)).start()

# الشروع في تشغيل السيرفر عند تنفيذ البرنامج كبرنامج مستقل
if __name__ == '__main__':
    start_server('localhost', 8888)