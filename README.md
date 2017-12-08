# Nanoleaf Standup Generator

## Setup

Create a development virtualenv with:

```
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Nanoleaf discovery

Run `discover.py` to find the IP of your Nanoleaf device. This can be temperamental, and might take a few tries.

After this, copy the `example-manifest.yml` file to `manifest.yml`, and replace the IP address with the discovered IP of your Nanoleaf device.

Next run `auth.py`, and add the correct token to your manifest. To authenticate you need to hold down the power button of the Nanoleaf for 5-7 seconds, until the LED light on the controller flashes.
