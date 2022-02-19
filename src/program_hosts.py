from colorama import Fore
from infrastructure.switchlang import switch
import infrastructure.state as state
from services import data_service as svc

def run():
    print(' ****************** Welcome host **************** ')
    print()

    show_commands()

    while True:
        action = get_action()

        with switch(action) as s:
            s.case('c', create_account)
            s.case('a', log_into_account)
            s.case('l', list_cages)
            s.case('r', register_cage)
            s.case('u', update_availability)
            s.case('v', view_bookings)
            s.case('m', lambda: 'change_mode')
            s.case(['x', 'bye', 'exit', 'exit()'], exit_app)
            s.case('?', show_commands)
            s.case('', lambda: None)
            s.default(unknown_command)

        if action:
            print()

        if s.result == 'change_mode':
            return


def show_commands():
    print('What action would you like to take:')
    print('[C]reate an account')
    print('Login to your [a]ccount')
    print('[L]ist your cages')
    print('[R]egister a cage')
    print('[U]pdate cage availability')
    print('[V]iew your bookings')
    print('Change [M]ode (guest or host)')
    print('e[X]it app')
    print('[?] Help (this info)')
    print()


def create_account():
    print(' ****************** REGISTER **************** ')

    name = input('What is your name? ')
    email = input('What is your email? ').strip().lower()
    # here we'll check if account exists already
    old_account = svc.find_account_by_email(email)
    
    if old_account:
        print(f'ERR: account {email} already exists!')
        return
    state.active_account =  svc.create_account(name, email)
    print(f'created new account with {state.active_account.id()}')

def log_into_account():
    print(' ****************** LOGIN **************** ')

    email = input('What is your email?').strip().lower()
    account = svc.find_account_by_email(email)
    
    if not account:
        print('Could not find account with email {}'.format(email))
        return
    
    state.active_account = account
    print('Logged in successfully')


def register_cage():
    print(' ****************** REGISTER CAGE **************** ')

    if not state.active_account:
        print('You must login first to register a cage.')
        return
    
    square_meters = input('How many square meters is the cage? ')
    if not square_meters:
        print('Cancelled.')
        return
    
    square_meters = float(square_meters)
    carpeted = input('Is it carpeted [y, n]? ').lower().startswith('y')
    has_toys = input('Does it have toys [y, n]? ').lower().startswith('y')
    allows_dangerous = input('Can you host venomous snakes [y, n]? ').lower().startswith('y')
    name = input('Give your cage a name: ')
    price = input('How much does this cage cost? $')
    price = float(price)
    cage = svc.register_cage(
        state.active_account, square_meters, carpeted, 
        has_toys, allows_dangerous, name, price
        )
    
    state.reload_account()
    print(f'Registered new cage with id {cage.id}')


def list_cages(supress_header=False):
    if not supress_header:
        print(' ******************     Your cages     **************** ')

    if not state.active_account:
        print('You must login first to register a cage.')
        return
    
    cages = svc.find_cages_for_user(state.active_account)
    print(f'You have {len(cages)} cages.')
    for c in cages:
        print(f' # {c.name} is {c.square_meters} meters. ')


def update_availability():
    print(' ****************** Add available date **************** ')

    # TODO: Require an account
    # TODO: list cages
    # TODO: Choose cage
    # TODO: Set dates, save to DB.

    print(" -------- NOT IMPLEMENTED -------- ")


def view_bookings():
    print(' ****************** Your bookings **************** ')

    # TODO: Require an account
    # TODO: Get cages, and nested bookings as flat list
    # TODO: Print details for each

    print(" -------- NOT IMPLEMENTED -------- ")


def exit_app():
    print()
    print('bye')
    raise KeyboardInterrupt()


def get_action():
    text = '> '
    if state.active_account:
        text = f'{state.active_account.name}> '

    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()


def unknown_command():
    print("Sorry we didn't understand that command.")


def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)


def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)
