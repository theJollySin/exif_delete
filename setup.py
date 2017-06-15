from setuptools import setup

readme_file = open("README.md", "r").read()

setup(
    name = "exif_delete",
    version = "0.9.0",
    author = "John Stilley",
    description = ("A simple tool to remove the EXIF data from image files."),
    license = "GPLv3",
    keywords = "exif delete python",
    url = "https://github.com/theJollySin/exif_delete",
    scripts=['exif_delete.py'],
    long_description=readme_file,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Utilities",
    ],
)
