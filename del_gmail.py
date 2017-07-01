import email
import imaplib
import ctypes
import getpass
mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
unm = raw_input('Please enter your gmail: ')
pwd = getpass.getpass('Password: ')

mail.login(unm,pwd)
mail.select('INBOX')

typ, data = mail.search(None, 'UNSEEN')
for num in data[0].split():
        mail.store(num, '+FLAGS', '\\Deleted')

