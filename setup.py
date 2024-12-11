from setuptools import setup, find_packages

setup(
    name='anki_gendeck_cli',
    version='1.0.0',
    description='A CLI tool for generating Anki decks from plain text.',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'anki-gendeck=anki_gendeck_cli.deck_from_plain_text:main',
        ],
    },
    install_requires=[
        'requests',
        'beautifulsoup4',
        'lxml',
    ],
    python_requires='>=3.6',
)
