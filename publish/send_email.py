# coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送者邮箱
SENDER = 'junkili@163.com'
# 发送者的登陆用户名和密码
USER = 'junkili'
PASSWORD = 'EzbuyBest1'
# 发送者邮箱的SMTP服务器地址
SMTPSERVER = 'smtp.163.com'


def send_email(subject, receivers, content):
    # 构造纯文本邮件内容
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = SENDER
    msg['To'] = ";".join(receivers)
    print 'msg : '
    print msg
    smtp = smtplib.SMTP()  # 实例化SMTP对象
    smtp.connect(SMTPSERVER, 25)  # （缺省）默认端口是25 也可以根据服务器进行设定
    smtp.login(USER, PASSWORD)  # 登陆smtp服务器
    smtp.sendmail(SENDER, receivers, msg.as_string())
    smtp.quit()


if __name__ == "__main__":
    receiver_list = ['huangyao@ezbuy.com']
    file_name = sys.argv[1]
    with open(file_name) as fo:
        mail_content = fo.read()
    send_email(u'python SMTP 测试邮件', receiver_list, mail_content)
