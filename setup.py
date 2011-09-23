# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

from setuptools import setup, find_packages


setup(
    name='gocept.bender',
    version='0.1dev',
    author='Wolfgang Schnerring',
    author_email='ws@gocept.com',
    url='http://packages.python.org/gocept.bender',
    description="""A Jabber-Bot that can be told things to say via XML-RPC.
""",
    long_description=(
        open('README.txt').read()
        + '\n\n'
        + open('CHANGES.txt').read()),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='ZPL',
    namespace_packages=['gocept'],
    install_requires=[
        'setuptools',
        'jabberbot',
        'xmpppy', # jabberbot doesn't declare
    ],
    extras_require=dict(test=[
    ]),
)
