import smtplib , csv , ssl
#support@jonassoftwaresupport1612463841.zendesk.com

smtp_server = 'smtp.gmail.com'
port = 465

sender = 'test.zd102@gmail.com'
password = input(' Please enter your password: ')
receiver = 'support@jonassoftwaresupport1612463841.zendesk.com'
message = """\
From: {}
To:   {}
Subject: Hi There!

This is sent automatically
""".format(sender, receiver)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)




