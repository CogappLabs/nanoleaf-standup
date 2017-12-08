import os
from time import sleep
from nanoleaf import Aurora
from nano_standup.credentials import load_manifest
from nano_standup.generate import set_static_layout

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
manifest = load_manifest(BASE_PATH)

print('Connecting to the Nanoleaf at {!s}'.format(manifest['nanoleaf']['ip']))

my_aurora = Aurora(manifest['nanoleaf']['ip'], manifest['nanoleaf']['token'])
my_aurora.on = True
my_aurora.effect = "Drupal"

sleep(2)

standup_panels = list()

for name, panel_data in manifest['panels'].items():
    data = {'id': panel_data['id']}
    data.update(panel_data['rgb'])
    standup_panels.append(data)

my_aurora.effect_set_raw(set_static_layout(standup_panels))

