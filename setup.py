import setuptools

VERSION = "0.0.2"

setuptools.setup(
    name="pygame_button",
    version=VERSION,
    py_modules=["pygame_button"],
    url="",
    license="GPLv3",
    author="Layerex",
    author_email="layerex@dismail.de",
    description="A very simple button class for pygame",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["pygame"],
    classifiers=[
        "Development Status :: 7 - Inactive",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: pygame",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)
