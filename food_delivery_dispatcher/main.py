from . import worker
from . import tables
import logging

logger = logging.getLogger(__name__)

def main():
    ''' the main entry point '''
    tables.create_all()
    worker.dispatch()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
