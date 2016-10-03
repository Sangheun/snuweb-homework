import smtplib

from getpass import getpass

sender = 'xiangxin0108@naver.com'
receiver = 'xiangxin0108@naver.com'
password = getpass('Enter Password :')
subject = '테스트 메일'
message = '''테스트
테스트
테스트
'''
server = smtplib.SMTP_SSL('smtp.naver.com', 465)
server.login(sender, password)
body = '''To: {}

From: {}

Subject: {}

{}'''.format(receiver, sender, subject, message)
server.sendmail(sender, [receiver], body.encode('utf8'))
server.quit()
print('sended!')
