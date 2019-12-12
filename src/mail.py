from err import *
import readline

class Mail:
    def __init__(self, src, txt):
        self.src = src
        self.txt = txt

    def __str__(self):
        i = self.txt.find('\n')
        if i == -1 and len(self.txt) < 50:
            i = 45
        summary = self.txt[:i] + '(...)'
        return 'From: {} "{}"'.format(self.src, summary)

    def read(self):
        print('--- From: {} ---'.format(self.src))
        print(self.txt)

class MailBox:
    def __init__(self):
        self.unread = []
        self.old = []

    def checkMail(self):
        print('You have {} new messages.'.format(len(self.unread)))
        print('Type `read-new-mails` to see them.')

    def readNewMails(self):
        print('Press Ctrl+D or Ctrl+C to cancel, Enter for next message')
        try:
            while self.unread:
                msg = self.unread.pop(0)
                msg.read()
                self.old.append(msg)
                input()
        except (EOFError, KeyboardInterrupt):
            pass
        print('No more new messages')

    def oldMail(self):
        print('--- Old messages: ---')
        for i in range(len(self.old)):
            msg = self.old[i]
            print('[{}] {}'.format(i, msg))

    def readOldMail(self, i):
        try:
            i = int(i)
            msg = self.old[i]
            msg.read()
        except:
            err('read-mail: invalid ID')

    def deleteMail(self, i):
        try:
            i = int(i)
            self.old.pop(i)
        except:
            err('delete-mail: invalid ID')

    def sendMail(self, src, dst):
        txt = ''
        print('Write your message to {}. Press Ctrl+D to send, Ctrl+C to cancel.\n---'.format(dst))
        try:
            txt += input()
            while True:
                txt += '\n' + input()
        except EOFError:
            print('---\nMail sent.')
            dst.inbox.unread.append(Mail(src, txt))
        except KeyboardInterrupt:
            print('---\nOperation canceled.')
