import smtplib
import email.mime.multipart
import email.mime.text

def sendEmail(mail,subject,content):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = 'CS Market 官方邮件'
    msg['to'] = mail
    msg['subject'] = subject
    content = content
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    smtp = smtplib
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com', '25')
    smtp.login('thinkgamer@163.com', 'your_passwd')
    smtp.sendmail('thinkgamer@163.com', mail, str(msg))
    smtp.quit()
    return 1