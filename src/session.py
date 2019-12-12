from err import *
from user import *
import readline

class Session:
    def __init__(self):
        self.currentUser = User()
        self.users = {}

    def login(self, args):
        if len(args) < 2:
            err('login: no name given')
            return

        name = args[1]
        user = self.users.get(name)
        if user is None:
            print('Creating user {}'.format(name))
            user = User(name)
            self.users[name] = user

        elif not user.checkPassword():
            err('login: wrong password')
            return

        self.currentUser = user
        user.greet()

    def logout(self, args = []):
        self.currentUser.sayBye()
        self.currentUser = User()

    def deleteAccount(self, args = []):
        name = self.currentUser.name
        s = input('Are you sure you want to delete account of {}? (type `yes` to confirm): '.format(name))
        if s != 'yes':
            return
        self.users.pop(name)
        self.currentUser = User()
        print('Deleted')

    def loggedIn(self, show = True):
        if self.currentUser.name:
            return True

        if show:
            err('not logged in')

        return False

