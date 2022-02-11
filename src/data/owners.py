class Owner:
    registered_date = None
    name = None
    email = None

    snake_ids = list() #TODO: create an id module/dict for different pets
    cage_ids = list()

    meta = {
        'db_alias': 'core',
        'collection': 'owners'
        }
