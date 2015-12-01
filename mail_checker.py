#!/usr/bin/python
# Retrieving POP3 Email with poplib
import imaplib, getpass, os
def main():
    path = os.environ['HOME'] + "/.mail.txt"
    with open(path, "r", encoding='utf-8') as in_f:
        for line in in_f:
            username, password = line.strip().split(':')
    gmail = imaplib.IMAP4_SSL('imap.gmail.com', '993')
    gmail.login(username, password)
    # Select the incoming unread messages
    typ, count = gmail.select('INBOX')
    # Displays incoming unread messages
    messageCount = len(gmail.search(None, 'UnSeen')[1][0].split())
    print(messageCount)
    # Close currently selected mailbox.
    gmail.close()
    # Shutdown connection to server. Returns server BYE response.
    gmail.logout()
# Run the programm
main()
