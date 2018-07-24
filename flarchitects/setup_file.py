from setuptools import setup

setup(
    name='app_name',
    version='1.0',
    long_description=__doc__,
    packages=['app_name'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask',]
)
