import os
from time import sleep

STANDUP_FILE = '/tmp/standup_participants.txt'
PHP_STANDUP_FILE = '/tmp/standup.txt'

def standups_remaining(participants):
    for name, participant_data in participants.items():
        if not participant_data['stood_up']:
            return True

    return False


def do_standup_interstitial(aurora):
    aurora.effect = 'Blockbusters'
    sleep(3)

def do_standup_round(aurora, names, participant_data, stood_up=list()):
    first = True
    standup_participant = None
    standup_panels = list()

    for name in names:
        panel_data = participant_data[name]
        data = {'id': panel_data['id']}

        if first and name not in stood_up and not panel_data['stood_up']:
            data.update(panel_data['rgb'])
            participant_data[name]['stood_up'] = True
            print('Standing up {!s}'.format(name))
            standup_participant = name
            first = False
        else:
            data.update({
                'R': 0,
                'G': 0,
                'B': 0,
            })

        standup_panels.append(data)

    panels_not_used = [105, 126, 133]

    for panel in panels_not_used:
        standup_panels.append({
                'id': panel,
                'R': 0,
                'G': 0,
                'B': 0,
            })


    aurora.effect_set_raw(set_static_layout(standup_panels))

    return standup_participant


def reset_standup(aurora, participant_data):
    standup_panels = list()

    for name, name_data in participant_data.items():
        data = {'id': name_data['id']}
        data.update({
            'R': 0,
            'G': 0,
            'B': 0,
        })

        standup_panels.append(data)

    aurora.effect_set_raw(set_static_layout(standup_panels))


def set_static_layout(panel_data):
    """
    Construct and initialise a static layout.

    :param panel_data:
        An ordered list of panel data dicts. Expects each dict to be of the format:
        {
            'id': 123,
            'R': 255,
            'G': 255,
            'B': 255,
        }

        For now numFrames is 1, W is 0 and T is 1. These are not configurable.
    :return:
    """
    num_panels = str(len(panel_data))

    effect = list()
    effect.append(num_panels)

    for panel in panel_data:
        effect.append(str(panel['id']))
        effect.append('1')  # numFrames
        effect.append(str(panel['R']))
        effect.append(str(panel['G']))
        effect.append(str(panel['B']))
        effect.append('0')  # W
        effect.append('1')  # TR

    message = {
        "command": "add",
        "version": "1.0",
        "animName": "Test",
        "animType": "static",
        "animData": ' '.join(effect),
        "loop": False,
    }

    return message


def clear_php_standup():
    if os.path.exists(PHP_STANDUP_FILE):
        os.remove(PHP_STANDUP_FILE)


def clear_standup():
    if os.path.exists(STANDUP_FILE):
        os.remove(STANDUP_FILE)


def get_standup_participants():
    if not os.path.exists(STANDUP_FILE):
        return list()
    else:
        with open(STANDUP_FILE, 'r', encoding='utf-8') as fh:
            participants = fh.read().split('\n')
            return list(filter(None, participants))


def add_standup_participant(name):
    with open(STANDUP_FILE, 'a', encoding='utf-8') as fh:
        fh.write(name + '\n')