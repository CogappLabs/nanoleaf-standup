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

    return ' '.join(effect)
