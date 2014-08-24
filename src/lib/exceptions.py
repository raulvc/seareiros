# -*- coding: UTF-8 -*-
#from time import sleep


class StockOverflowException(Exception):
    """
        Indicates that a book quantity exceeded it's stock
    """
    pass

class RecordNotFoundException(Exception):
    """
        Indicates that a book quantity exceeded it's stock
    """
    pass

class DbUnavailableException(Exception):
    """
        Indicates that a book quantity exceeded it's stock
    """
    pass