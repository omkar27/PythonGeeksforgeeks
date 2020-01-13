import imaplib
import pprint
import email
import datetime
imap_host = 'imap.gmail.com'
imap_user = 'dummyomkar@gmail.com'
imap_pass = 'Omkar27@dummy'

# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

## login to server
imap.login(imap_user, imap_pass)

imap.select('Inbox',readonly=True)

result, data = imap.uid('search', None, "SEEN") # (ALL/UNSEEN)
i = len(data[0].split())
print i

for x in range(i):
    latest_email_uid = data[0].split()[x]
    result, email_data = imap.uid('fetch', latest_email_uid, '(RFC822)')
    # result, email_data = conn.store(num,'-FLAGS','\\Seen')
    # this might work to set flag to seen, if it doesn't already
    raw_email = email_data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)

    # Header Details
    date_tuple = email.utils.parsedate_tz(email_message['Date'])
    if date_tuple:
        local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
        local_message_date = "%s" % (str(local_date.strftime("%a, %d %b %Y %H:%M:%S")))
    email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
    email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
    subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))

    # Body details
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            file_name = "email_" + str(x) + ".txt"
            output_file = open(file_name, 'w')
            output_file.write("From: %s\nTo: %s\nDate: %s\nSubject: %s\n\nBody: \n\n%s" % (
            email_from, email_to, local_message_date, subject, body.decode('utf-8')))
            output_file.close()
        else:
            continue
# tmp, data = imap.search(None, 'ALL')
# for num in data[0].split():
# 	tmp, data = imap.fetch(num, '(RFC822)')
# 	print('Message: {0}\n'.format(num))
# 	pprint.pprint(data[0][1])
# 	break
imap.close()