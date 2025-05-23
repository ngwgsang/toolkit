from setuptools import setup, find_packages

setup(
    name='toolkit',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "typing",
    ],
    author='Sang Quang Nguyen',
    description='A reusable toolkit with some bug',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
