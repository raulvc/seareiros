days_of_the_week = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']

# Kinds of books to display
BOOK_ALL, BOOK_SELL, BOOK_RENT = range(3)

# Permissions
access_table = [
    # Forms
    'actionAddAssociate', 'actionAddBook', 'actionAddProduct', 'actionAddActivity',
    # Orders
    'actionSellBook', 'actionSellProduct', 'actionSellEvent',
    # Library
    'actionLibLend', 'actionLibReturn',
    # Reports
    'actionRepSales', 'actionRepLibrary', 'actionRepProduct', 'actionRepBook',
    # Pendencies
    'actionPendencies'
]