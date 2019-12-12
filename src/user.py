from err import *
from mail import MailBox

from getpass import getpass
import readline

class User:
    def __init__(self, name = None):
        self.name = name
        self.inbox = MailBox()
        if name:
            self.setPassword()

    def checkPassword(self):
        pwd = getpass()
        return self.pwd == pwd

    def sayBye(self):
        print('Bye {}'.format(self.name))

    def greet(self):
        print('Hi {}!'.format(self.name))

    def setPassword(self):
        self.pwd = getpass()

    def checkPassword(self):
        pwd = getpass()
        return self.pwd == pwd

    def sayBye(self):
        print('Bye {}'.format(self.name))
