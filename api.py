import random
from flask import Flask

from worker import process_file


app = Flask(__name__)

@app.route('/')
def root():
    n = random.randrange(1, 10)
    process_file.delay(n)
    return f'Sent task to worker which will take {n} seconds to complete!'


if __name__ == "__main__":
    app.run()