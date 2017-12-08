import os
from nanoleaf import setup
from nano_standup.credentials import load_manifest

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
manifest = load_manifest(BASE_PATH)

token = setup.generate_auth_token(manifest['nanoleaf']['ip'])
