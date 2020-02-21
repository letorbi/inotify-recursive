import setuptools
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = ["inotify-simple"]

# The enum34 requirement should be handled by inotify-simple
if sys.version_info.major < 3 or (sys.version_info.major == 3 and sys.version_info.minor < 4):
    install_requires += ["enum34"]

setuptools.setup(
    name="inotifyrecursive",
    version="0.2.6",
    author="Torben Haase",
    author_email="torben@pixelsvsbytes.com",
    description="Recursive inotify watches based on inotify_simple.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/letorbi/inotifyrecursive",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    install_requires=install_requires,
)
