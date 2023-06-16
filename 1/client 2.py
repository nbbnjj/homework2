import socket

# تابع لإجراء الاختبار
def take_quiz(sock):
    # حلقة لتلقي الأسئلة وإرسال الإجابات
    while True:
        # تلقي السؤال من السيرفر
        question = sock.recv(1024).decode()
        # التأكد من عدم وجود رسالة فارغة
        if not question:
            break
        # طلب الإجابة من المستخدم
        answer = input(question + '\n')
        # إرسال الإجابة إلى السيرفر
        sock.sendall(answer.encode())
    # تلقي النتيجة من السيرفر وطباعتها
    score = sock.recv(1024).decode()
    print(score)

# تابع لبدء العميل
def start_client(host, port):
    # إنشاء socket عميل والاتصال به بالمضيف والمنفذ المحددين
    csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    csock.connect((host, port))
    # إجراء الاختبار باستخدام التابع take_quiz()
    take_quiz(csock)
    # إغلاق الاتصال
    csock.close()

# الشروع في تشغيل العميل عند تنفيذ البرنامج كبرنامج مستقل
if __name__ == '__main__':
    start_client('localhost', 8888)