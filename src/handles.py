from session import *
from err import *
import pickle

class QuitException(Exception):
    pass

def myQuit(args):
    raise QuitException()

def myHelp(args):
    print('Available commands:')
    for cmd in dispatch.keys():
        print(cmd)

def unknown(args):
    err('unknown command {}. Try `help`'.format(args[0]))

def hi(args):
    session.currentUser.greet()

def changePassword(args):
    session.currentUser.setPassword();

def checkMail(args):
    session.currentUser.inbox.checkMail()

def readNewMails(args):
    session.currentUser.inbox.readNewMails()

def oldMail(args):
    session.currentUser.inbox.oldMail()

def readMail(args):
    if len(args) < 2:
        err('you must specify the ID of the mail you want to read')
        return
    session.currentUser.inbox.readOldMail(args[1])

def deleteMail(args):
    if len(args) < 2:
        err('you must specify the ID of the mail you want to delete')
        return
    session.currentUser.inbox.deleteMail(args[1])

def sendTo(args):
    if len(args) < 2:
        err('you must specify the name of the recipient')
        return
    dst = session.users.get(args[1])
    if not dst:
        err('user {} does not exist'.format(args[1]))
        return
    session.currentUser.inbox.sendMail(currentUser.name, dst)

try:
    f = open('pyshell.session', 'rb')
    session = pickle.load(f)
    f.close()
except (FileNotFoundError, EOFError):
    session = Session()

dispatch = {
    'quit': myQuit,
    'help': myHelp,
    'login': session.login,
    'logout': session.logout,
    'delete-account': session.deleteAccount,
    'hi': hi,
    'change-password': changePassword,
    'check-mail': checkMail,
    'read-new-mails': readNewMails,
    'old-mail': oldMail,
    'read-mail': readMail,
    'delete-mail': deleteMail,
    'send-to': sendTo,
}
