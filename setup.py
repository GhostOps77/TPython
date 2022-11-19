from setuptools import setup

classifiers = [
    "Development Status :: 4 - Beta",
    'Environment :: Console',
    "Intended Audience :: Developers :: Education :: Other Audience",
    "Programming Language :: Python :: 3.6",
    "License :: OSI Approved :: MIT License"
]

with open('README.md', 'r') as f:
    ld = f.read()

if __name__ == '__main__':
    setup(
    name='TPython',
    version="0.1",
    description='A better python REPL',
    long_description=ld,
    long_description_content_type='text/markdown',
    url='https://github.com/Techlord210/TPython',
    author='Techlord210',
    author_email='techlord210@gmail.com',
    license='MIT', 
    classifiers=classifiers,
    keywords='interactive,python,better,repl,tpython', 
    packages=[],
    install_requires=['colorama']
    )