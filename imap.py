import email
import imaplib

username = "dummyomkar@gmail.com"
password = "Omkar27@dummy"

mail = imaplib.IMAP4_SSL("smtp.gmail.com")
mail.login(username,password)
mail.select("Inbox")
#create new folder
mail.create("Item2")
print mail.list()
result,data = mail.uid('search', None,'All')
print data[0].split()
inbox_item = data[0].split()
recent = inbox_item[-1]
older = inbox_item[0]
result2,data = mail.uid('fetch',recent,'(RFC822)')
raw_email = data[0][1]
email_message = email.message_from_string(raw_email)
print email_message['To']
print email_message['From']
print email_message['Subject']
mail.logout()
#print data
