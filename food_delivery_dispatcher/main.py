from . import worker
from . import tables

def main():
    tables.create_all()
    worker.dispatch()

if __name__ == '__main__':
    main()
