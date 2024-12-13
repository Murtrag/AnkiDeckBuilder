from setuptools import setup, find_packages

setup(
    name='anki_gendeck_cli',
    version='1.0.0',
    description='A CLI tool for generating Anki decks from plain text.',
    install_requires=[
        'beautifulsoup4==4.12.3',
        'bs4==0.0.2',
        'cached-property==2.0.1',
        'certifi==2024.8.30',
        'charset-normalizer==3.4.0',
        'chevron==0.14.0',
        'frozendict==2.4.6',
        'genanki==0.13.1',
        'idna==3.10',
        'PyYAML==6.0.2',
        'requests==2.32.3',
        'soupsieve==2.6',
        'urllib3==2.2.3',
    ],
    python_requires='>=3.6',
)