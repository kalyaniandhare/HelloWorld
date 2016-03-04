#import sys
import imaplib
imaplib._MAXLINE = 200000
from .models import Extractore, StoreData
import email
import datetime
IMAP_SERVER = 'imap.gmail.com'
import re
import xlrd


def get_filedata(path):

      book = xlrd.open_workbook(path)
      print(book.nsheets)
      print(book.sheet_names())
      first_sheet = book.sheet_by_index(0)
      print(first_sheet.row_values(1))
      cell = first_sheet.cell(1,0)
      print(cell)
      print(cell.value)


def process_mailbox(M):
    """
    Dump all emails in the folder to files in output directory.
    """

    #rv, data = M.search(None, "ALL")
    rv, data = M.search(None,  'FROM', '"Ritesh Nikam"')

    if rv != 'OK':
        print("No messages found!")
        return

    num = data[0].split()[-2]
    rv, data = M.fetch(num, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)

    #print(email_message)
    #print("!!!",email_message['Subject'],'\n')
    #print(email_message['Date'],"T")
    #print(email_message['To'])
    #print(email.utils.parseaddr(email_message['From'])) # for parsing "Yuji Tomita" <yuji@grovemade.com>
    #print(email_message.get_payload()) # print all headers

    maintype = email_message.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message.walk():
            print("1")
            if part.get_content_maintype() == 'multipart': continue
            if part.get('Content-Disposition') is None: continue
            filename = part.get_filename()
            fp = open(filename, 'wb')
            fp.write(part.get_payload(decode=True))
            get_filedata(filename)
            fp.close()

    list1 ={'username': str(re.findall("(.*)\<",email_message['To'])[0].rstrip()),
                  'useremailid': re.findall("<(.*)>",email_message['To'])[0],
                  'email_from': re.findall("<(.*)>",email_message['From'])[0],
                  'email_to': re.findall("<(.*)>",email_message['To'])[0],
                  'date': datetime.datetime.now(),
                  'subject': email_message['Subject'],
                  'filename': "fname",
                  'filedata': "NA", }
    return list1


def login_to_user(userid,password):

      print(userid,password)
      M = imaplib.IMAP4_SSL(IMAP_SERVER)
      M.login(userid,password)
      rv, data = M.select("Inbox")
      if rv == 'OK':
            list1 = process_mailbox(M)
            M.close()

      else:
            print("ERROR: Unable to open mailbox ", rv)
            M.logout()

      return list1


def save_data(value):
      user = StoreData(**value)
      user.save()
      print("...",user.email_from)
      return user

def get_data(u_id,password):
      list1 = login_to_user(u_id,password)
      user = save_data(list1)
      return user
