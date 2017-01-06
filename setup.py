from setuptools import setup, find_packages

setup(
    name = "Greengraph",
    version = "1.0.0",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/greengraph'],
    install_requires = ['argparse', 'numpy', 'geopy', 'matplotlib', 'requests']
)
