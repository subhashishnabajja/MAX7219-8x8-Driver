from setuptools import setup, find_packages
import re

REPO_URL = "https://github.com/subhashishnabajja/MAX7219-8x8-Driver"

def read_description():
    with open("README.md") as f:
        header = "For more information, see the [GitHub Repository]" \
                 "({0}).".format(REPO_URL)
        filter_re = re.compile(r'.*\bPyPI\b.*')
        contents = header + "\n" + filter_re.sub("", f.read())
        return contents.strip()
    

VERSION = '0.0.2'
DESCRIPTION = 'This Package contains the code required to drive a max7219 8x8 LED matrix using a Raspberry Pi (with `spidev`).'

# Setting up
setup(
    name="max7219-driver",
    version=VERSION,
    author="Subhashish Nabajja",
    author_email="<subhashishnabajja619@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=read_description(),
    packages=find_packages(),
    install_requires=["spidev"],
    keywords=["Max7219", "Led Matrix", "Raspberry Pi", "8x8 Matrix"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ]
)
