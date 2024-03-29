from setuptools import setup, find_packages


setup(
    name='gocept.bender',
    version='1.1dev',
    author='gocept gmbh & co. kg',
    author_email='mail@gocept.com',
    url='https://bitbucket.org/gocept/gocept.bender',
    description="""A Jabber-Bot that can be told things to say via XML-RPC.
""",
    long_description=(
        open('README.txt').read() +
        '\n\n' +
        open('CHANGES.txt').read()),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='ZPL',
    namespace_packages=['gocept'],
    install_requires=[
        'dnspython',  # xmpp doesn't declare
        'jabberbot',
        'setuptools',
        'xmpppy',  # jabberbot doesn't declare
        'zope.component',
        'zope.event',
    ],
    extras_require=dict(test=[
        'mock',
    ]),
    entry_points=dict(console_scripts=[
        'bender-server = gocept.bender.bot:main',
    ]),
)
