import os
from nanoleaf import Aurora
from nano_standup.credentials import load_manifest

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
manifest = load_manifest(BASE_PATH)

my_aurora = Aurora(manifest['nanoleaf']['ip'], manifest['nanoleaf']['token'])
my_aurora.on = True

for panel in my_aurora.panel_positions:
  print(panel['panelId'])
