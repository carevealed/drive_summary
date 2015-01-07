# from distutils.core import setup
from setuptools import setup
setup(
    name='driveSummary',
    version='0.1.1',
    url='https://github.com/cavpp/drive_summary',
    license='MIT',
    author='Henry Borchers',
    author_email='hborcher@berkeley.edu',
    description='Written for the California AV Preservation Project, Utility to get a summary of the AV files on a '
                'given drive or folder',
    include_package_data=True,
    scripts=['bin/driveSummaryCLI.py', "bin/driveSummaryGUI.py"],
    packages=['driveSummary'],
    install_requires=['pip >= 6.0',
                      'setuptools >= 11.3',
                      'PySide >= 1.2.2']
)
