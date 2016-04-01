import sys
import time

class stderr_wrapper(object):
    def __init__(self, stderr_fn):
        self.my_stderr = open(stderr_fn, "w+")
    def write(self, error_string):
        self.my_stderr.write(time.ctime() +": "+ error_string)
sys.stderr = stderr_wrapper("/tmp/log")

if __name__ == '__main__':
    raise ArithmeticError("Tyler is wrong")
