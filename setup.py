from setuptools import setup, find_packages

setup(
    name='anki_gendeck_cli',
    version='1.0.0',
    description='',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cli-tool=cli_tool.cli:main',
        ],
    },
    install_requires=[
        # Lista zależności
    ],
    python_requires='>=3.6',
)
