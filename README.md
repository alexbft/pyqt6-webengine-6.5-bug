## About

Showcase of a bug specific to [PyQt6](https://pypi.org/project/PyQt6/) version 6.5.3 and below. It appears fixed in 6.6.0.

Requires 2 or more monitors (I've tested on both 4k and FullHD resolutions).
I have Windows 11 64 bit, not sure if this is related.
I've also added a flag to disable GPU acceleration (a suggested workaround, does not work).

Bug thread: https://bugs.launchpad.net/calibre/+bug/2043590

## Instructions
Make sure you have [pipenv](https://pipenv.pypa.io/en/latest/index.html) installed!
Clone the repo:

    git clone https://github.com/alexbft/pyqt6-webengine-6.5-bug.git

Run the code from the source dir:

	pipenv install
    pipenv run python main.py
You should have a window on your second monitor, appearing frozen.
![image](https://github.com/alexbft/pyqt6-webengine-6.5-bug/assets/537984/74aed72b-8417-482e-b7b8-b39334f556c7)

