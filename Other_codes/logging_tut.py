import logging

logging.basicConfig(filename='test.log', level=logging.INFO,format='%(asctime)s : %(levelname)s : %(message)s')
def add(*args):
    add = 0
    for i in args:
        add += i

    v = logging.getLogger(__name__)
    print(v)
    logging.info(add)
    return(add)

print(add(3,45,5,4))


