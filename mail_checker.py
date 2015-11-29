#!/usr/bin/python
# Retrieving POP3 Email with poplib
import imaplib, getpass, email
def main():
    gmail = imaplib.IMAP4_SSL('imap.gmail.com', '993')
    username = input('Login: ')
    password = getpass.getpass()
    gmail.login(username, password)
    # Select the incoming unread messages
    typ, count = gmail.select('INBOX')
    # Displays incoming unread messages
    typ, unseen = gmail.status('INBOX', "(UNSEEN)")
    print (unseen)
    # Close currently selected mailbox.
    gmail.close()
    # Shutdown connection to server. Returns server BYE response.
    gmail.logout()
# Run the programm
main()
