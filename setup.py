from setuptools import setup

with open('README.md', 'r') as f:
    LD = f.read()

with open('requirements.txt', 'r') as f:
    DEPENDENCIES = f.read().splitlines()

__version__ = '1.7'

if __name__ == '__main__':
    setup(
        name = 'TPython',
        version = __version__,
        description = 'A better python REPL',
        long_description = LD,
        long_description_content_type = 'text/markdown',
        url = 'https://github.com/Techlord210/TPython',
        author = 'Techlord210',
        author_email = 'techlord210@gmail.com',
        license = 'MIT',
        classifiers = [
                "Development Status :: 5 - Production/Stable",
                'Environment :: Console',
                "Intended Audience :: Developers",
                "Intended Audience :: Education",
                "Intended Audience :: Other Audience",
                "Programming Language :: Python :: 3",
                "Programming Language :: Python :: 3.6",
                "Programming Language :: Python :: 3.7",
                "Programming Language :: Python :: 3.8",
                "Programming Language :: Python :: 3.9",
                "Programming Language :: Python :: 3.10",
                "Programming Language :: Python :: 3.11",
                "License :: OSI Approved :: MIT License"
            ],
        install_requires = DEPENDENCIES,
        entry_points = {
            'console_scripts': [
                'tpy = tpy.tpy:main'
                ]
            },
        python_requires = ">=3.6"
    )