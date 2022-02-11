class Cage:
    registered_date = None

    name = None
    price = None
    square_meters = None
    is_captured = None
    has_toys = None
    allow_dangerous = None

    bookings = list()

    meta = {
        'db_alias': 'core',
        'collection': 'cages'
        }


