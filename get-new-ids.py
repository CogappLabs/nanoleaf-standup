from nanoleaf import Aurora
from nano_standup.credentials import load_manifest
import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
manifest = load_manifest(BASE_PATH)

print('Connecting to the Nanoleaf at {!s}'.format(manifest['nanoleaf']['ip']))

my_aurora = Aurora(manifest['nanoleaf']['ip'], manifest['nanoleaf']['token'])

current_panels = list()
available_panel_pool = list()

# panels currently loaded in the manifest, thus in use
for name in manifest['panels']:
    ids = manifest['panels'][name]['id']
    current_panels.append(ids)

# panels currently connected to Nanoleaf
for panel in my_aurora.panel_positions:
  available_panel_pool.append(panel['panelId'])

# Compare used and avilable panels and return the unused ids
new_panels = list([x for x in available_panel_pool if x not in current_panels])

print('Total number of connected panels:', len(available_panel_pool)) 
print('Number of unused panels:', len(new_panels)) 
print('Unused panel IDs:',new_panels)
