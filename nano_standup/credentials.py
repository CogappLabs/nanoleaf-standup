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

            for name, panel_data in manifest['panels'].items():
                rgb = panel_data['rgb'].split(' ')
                manifest['panels'][name]['rgb'] = {
                    'R': rgb[0],
                    'G': rgb[1],
                    'B': rgb[2],
                }
    except yaml.YAMLError as e:
        print('Error loading YAML: {!s}'.format(e))
    except Exception as e:
        print('Error loading manifest: {!s}'.format(e))

    return manifest
