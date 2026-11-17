import serial, time, csv, winsound, smtplib
from email.mime.text import MIMEText

MAIL_USER = "2723928190@qq.com"
MAIL_PASS = "pmezichwzmtkdcja"
MAIL_TO   = "2723928190@qq.com"

def send_mail(body):
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = "宿舍温度告警"
    msg['From'] = MAIL_USER
    msg['To'] = MAIL_TO

    s = smtplib.SMTP_SSL('smtp.qq.com', 465)
    s.login(MAIL_USER, MAIL_PASS)
    s.sendmail(MAIL_USER, [MAIL_TO], msg.as_string())
    s.close()

ser = serial.Serial('COM3', 115200, timeout=2)
ser.reset_input_buffer()

last_push = 0

with open('data.csv', 'a', newline='') as f:
    w = csv.writer(f)
    while True:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if ',' in line:
            t, h = line.split(',')
            now = time.strftime('%Y-%m-%d %H:%M:%S')
            w.writerow([now, t, h])
            f.flush()
            print(now, t, h)

            if float(t) > 30:
                print("!!! 温度过高:", t)
                winsound.Beep(1000, 500)

                if time.time() - last_push > 300:
                    try:
                        send_mail(f"温度过高: {t}℃  湿度: {h}%")
                        print("邮件已发送")
                    except Exception as e:
                        print("发送失败:", e)
                    last_push = time.time()
