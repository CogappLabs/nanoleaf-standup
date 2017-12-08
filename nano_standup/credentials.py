import os
import yaml


def load_manifest(base_dir):
    """
    Load a manifest file from the base directory.
    
    :param base_dir:
      The base directory containing the manifest file.
    :return: 
    """
    try:
        with open(os.path.join(base_dir, 'manifest.yml'), 'r') as m:
            manifest = yaml.load(m)
    except yaml.YAMLError as e:
        print('Error loading YAML: {!s}'.format(e))
    except Exception as e:
        print('Error loading manifest: {!s}'.format(e))

    return manifest
