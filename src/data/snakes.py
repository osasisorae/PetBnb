class Snake:
    ''' Our snake model'''

    registered_date = None
    species = None

    length = None
    name = None
    is_venomous = None

    meta = {
        'db_alias': 'core',
        'collection': 'snakes', # plural snakes gotten from the 'Snake' class
        }
