from handles import QuitException, unknown, session, dispatch
import readline
import pickle

try:
    print('Type `help` to see all available commands.')
    while True:
        s = input('> ')
        args = s.split(' ')
        if args and args[0] not in ('login', 'quit', 'help'):
            if not session.loggedIn():
                continue
        f = dispatch.get(args[0], unknown)
        f(args)

except EOFError:
    print('quit')
except QuitException:
    pass

f = open('pyshell.session', 'wb')
pickle.dump(session, f)
f.close()
