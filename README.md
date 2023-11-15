## About

Showcase of a bug specific to [PyQt6-webengine](https://pypi.org/project/PyQt6-WebEngine/) version 6.5.0. It appears fixed in 6.6.0.

Requires 2 or more monitors (I've tested on both 4k and FullHD resolutions).
I have Windows 11 64 bit, not sure if this is related.

## Instructions
Make sure you have [pipenv](https://pipenv.pypa.io/en/latest/index.html) installed!
Clone the repo:

    git clone https://github.com/alexbft/pyqt6-webengine-6.5-bug.git

Run the code from the source dir:

	pipenv install
    pipenv run python main.py
You should have a window on your second monitor, appearing frozen.
