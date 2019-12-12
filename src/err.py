from sys import stderr

def err(msg):
    print('Error: {}'.format(msg), file=stderr)
