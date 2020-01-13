import imaplib
import email

username = "dummyomkar@gmail.com"
password = "Omkar27@dummy"

mail = imaplib.IMAP4_SSL("smtp.gmail.com")
mail.login(username,password)
mail.select("Inbox")
result,data = mail.uid('search',None,'all')
print data[0]
email_list = data[0].split()
print "Lenght",len(data)
print "Email List",email_list
older = email_list[0]
result2,dmaildata = mail.uid('fetch',older,'(RFC822)')
print dmaildata[0][1]
mailcontent = email.message_from_string(dmaildata[0][1])
print mailcontent['To']
print dir(mailcontent)
