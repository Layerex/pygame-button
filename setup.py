import setuptools

VERSION = "0.0.2"


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="pygame_button",
    version=VERSION,
    py_modules=["pygame_button"],
    author="Layerex",
    author_email="layerex@dismail.de",
    description="A very simple button class for pygame.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Layerex/pygame_button",
    packages=setuptools.find_packages(),
    install_requires=["pygame"],
    classifiers=[
        "Development Status :: 7 - Inactive",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: pygame",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)
