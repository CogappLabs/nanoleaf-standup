import os
from nano_standup.credentials import load_manifest
from nano_standup.generate import set_static_layout
import yaml
from nanoleaf import Aurora

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
manifest = load_manifest(BASE_PATH)

print('Connecting to the Nanoleaf at {!s}'.format(manifest['nanoleaf']['ip']))



my_aurora = Aurora(manifest['nanoleaf']['ip'],manifest['nanoleaf']['token'])
my_aurora.on = True
my_aurora.effect = "Drupal"

panelData = list()

for panel,id in manifest['panels'].items():
    panelData.append({
            'id': id,
            'R': 255,
            'G': 255,
            'B': 255,
        })
    if panel == 'kayw':
        panelData.append({
            'id': id,
            'R': 28,
            'G': 255,
            'B': 0,
        })
    if panel == 'benk':
        panelData.append({
            'id': id,
            'R': 255,
            'G': 0,
            'B': 165,
        })
    if panel == 'path':
        panelData.append({
            'id': id,
            'R': 255,
            'G': 157,
            'B': 0,
        })
    if panel == 'louiser':
        panelData.append({
            'id': id,
            'R': 255,
            'G': 255,
            'B': 0,
        })
    if panel == 'neilh':
        panelData.append({
            'id': id,
            'R': 0,
            'G': 0,
            'B': 255,
        })


my_aurora.effect_set_raw(set_static_layout(panelData))

