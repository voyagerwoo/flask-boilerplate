import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


setup(
    name='flask-dockerize',
    version='1.0.0',
    include_package_data=True,
    zip_safe=False,
    cmdclass={'test': PyTest},
    install_requires=[
        'pytest',
        'flask',
        'gunicorn',
        'flask-cors',
    ],
    tests_require=['pytest-flask'],
)
