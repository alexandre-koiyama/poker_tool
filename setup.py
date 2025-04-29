from setuptools import setup, find_packages

setup(
    name='poker_tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'treys',
    ],
    author='Alexandre K',
    author_email='alexandre.koiyama@outlook.com',
    description='A poker win calculator using Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/alexandre-koiyama/poker_tool', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.7', 
)