import random
import argparse
from nanoleaf import Aurora
from nano_standup.utils import *
from nano_standup.credentials import load_manifest

parser = argparse.ArgumentParser(description='A standup command-line tool for the Nanoleaf.')
parser.add_argument('--start-standup', action='store_true', help='Start a new standup')
parser.add_argument('--continue-standup', action='store_true', help='Continue an existing standup')
parser.add_argument('--reset-standup', action='store_true', help='Reset an existing standup')
args = parser.parse_args()

interactive = True

if args.start_standup or args.continue_standup or args.reset_standup:
    interactive = False

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
manifest = load_manifest(BASE_PATH)

print('Connecting to the Nanoleaf at {!s}'.format(manifest['nanoleaf']['ip']))

my_aurora = Aurora(manifest['nanoleaf']['ip'], manifest['nanoleaf']['token'])
my_aurora.on = True
my_aurora.effect = "Drupal"

standup_panels = list()
standup_participants = manifest['panels']

standup_participants_by_name = list(standup_participants.keys())
random_startup_participants = list()

while len(standup_participants_by_name) > 0:
    name = random.choice(standup_participants_by_name)
    random_startup_participants.append(name)
    standup_participants_by_name.remove(name)

print('Initiating standup')

if interactive:
    while standups_remaining(standup_participants):
        carry_on = input('Continue stand up? Y/N: ')

        if carry_on.lower() == 'y':
            do_standup_interstitial(my_aurora)
            do_standup_round(my_aurora, random_startup_participants, standup_participants)
        if carry_on.lower() == 'n':
            exit()
else:
    if args.start_standup:
        print('Starting the standup')
        clear_standup()
        do_standup_interstitial(my_aurora)
        name = do_standup_round(my_aurora, random_startup_participants, standup_participants)
        add_standup_participant(name)
    elif args.continue_standup:
        print('Continuing the standup')

        if (len(get_standup_participants()) + 1) == len(standup_participants):
            clear_php_standup()

        do_standup_interstitial(my_aurora)
        name = do_standup_round(my_aurora, random_startup_participants, standup_participants, stood_up=get_standup_participants())
        add_standup_participant(name)

        # If we've gone through all the participants, clear the standup.
        if len(get_standup_participants()) == len(standup_participants):
            print('The last person has stood up')
            clear_standup()
    elif args.reset_standup:
        print('Resetting the standup')
        clear_standup()
        reset_standup(my_aurora, standup_participants)
