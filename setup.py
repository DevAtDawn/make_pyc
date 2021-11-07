from setuptools import setup
setup(
    name='make_pyc',
    version='0.0.1',
    packages=['make_pyc'],
    entry_points={
        'console_scripts': [
            'make_pyc=make_pyc.make_pyc:main'
        ]
    }
)
