import email
import imaplib

username = "dummyomkar@gmail.com"
password = "Omkar27@dummy"

mail = imaplib.IMAP4_SSL("smtp.gmail.com")
mail.login(username,password)
mail.select('Inbox')
result,data = mail.uid('search',None,'All')
print result

mail_list = data[0].split()
print mail_list
first = mail_list[0]
result2,data2 = mail.uid('fetch',first,'(RFC822)')
print data2
email_data = email.message_from_string(data2[0][1])
print email_data['Subject']