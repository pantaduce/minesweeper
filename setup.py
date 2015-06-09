from distutils.core import setup

setup(
    name='minesweeper',
    version='1.3.0',
    packages=['minesweeper',],
    url='http://github.com/kinegratii/minesweeper',
    license='GPLv2',
    author='kinegratii',
    author_email='kinegratii@gmail.com',
    description='A tkinter-based game for minesweeper.',
    data_files=[
        (
            'minesweeper/resource',
            [
                'minesweeper/resource/project.txt',
                'minesweeper/images/mine.ico'
            ]
        )
    ]
)
