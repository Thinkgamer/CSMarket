import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(mail,subject,content):
    msg = MIMEMultipart('alternative')
    msg['From'] = "thinkgamer@163.com"
    msg['To'] = mail
    msg['Subject'] = subject

    # 添加邮件内容
    text = MIMEText(content)
    msg.attach(text)

    server = smtplib.SMTP()
    server.connect('smtp.163.com')  # 163邮箱的SMTP服务器地址
    server.login('thinkgamer@163.com', 'your_password')  # 输入邮箱用户名和密码
    server.set_debuglevel(1)
    server.sendmail('thinkgamer@163.com', mail, msg.as_string())
    server.quit()
    return 1
