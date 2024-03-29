"""Context managers are mainly used to properly manage resources. 
The most common use of a context manager is the opening of a file: with open('workfile', 'r') as f:"""

from time import time


class Timer():
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time()
        return None  # could return anything, to be used like this: with Timer("Message") as value:

    def __exit__(self, type, value, traceback):
        elapsed_time = (time() - self.start) * 1000
        print(self.message.format(elapsed_time))


with Timer("Elapsed time to compute some prime numbers: {}ms"):
    primes = []
    for x in range(2, 500):
        if not any(x % p == 0 for p in primes):
            primes.append(x)
    print("Primes: {}".format(primes))




class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Usage of the context manager
with FileHandler('example.txt', 'w') as file:
    file.write('This is an example.')

# At this point, the file is automatically closed, even if an exception occurs
