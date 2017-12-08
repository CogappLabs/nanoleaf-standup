import os
from time import sleep
from nanoleaf import Aurora
from nano_standup.credentials import load_manifest
from nano_standup.generate import set_static_layout


def standups_remaining(participants):
    for name, participant_data in participants.items():
        if not participant_data['stood_up']:
            return True

    return False

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
manifest = load_manifest(BASE_PATH)

print('Connecting to the Nanoleaf at {!s}'.format(manifest['nanoleaf']['ip']))

my_aurora = Aurora(manifest['nanoleaf']['ip'], manifest['nanoleaf']['token'])
my_aurora.on = True
my_aurora.effect = "Drupal"

standup_panels = list()
standup_participants = manifest['panels']

print('Initiating standup')

while standups_remaining(standup_participants):
    sleep(1)
    first = True
    current_name = None

    for name, panel_data in standup_participants.items():
        data = {'id': panel_data['id']}

        if first and not panel_data['stood_up']:
            data.update(panel_data['rgb'])
            standup_participants[name]['stood_up'] = True
            print('Standing up {!s}'.format(name))
            first = False
        else:
            data.update({
                'R': 255,
                'G': 255,
                'B': 255,
            })

        standup_panels.append(data)

    my_aurora.effect_set_raw(set_static_layout(standup_panels))
