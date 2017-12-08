import os
import yaml

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(BASE_PATH, 'manifest.yml'), 'r') as m:
        manifest = yaml.load(m)
except yaml.YAMLError as e:
    print('Error loading YAML: {!s}'.format(e))
except Exception as e:
    print('Error loading manifest: {!s}'.format(e))

print('Connecting to the Nanoleaf at {!s}'.format(manifest['nanoleaf']['ip']))
