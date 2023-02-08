from setuptools import setup, find_packages

setup(
    name='Project Name',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    description='A brief description of your project',
    author='Maxwell Mullin',
    author_email='mullinmax@gmail.com',
	python_requires='>=3.6',
    install_requires=[
        pytest
    ],
	extras_require={
        'build': [
            # dependencies required for building your package
        ],
        'test': [
            # dependencies required for testing your package
            'pytest'
        ],
    },
)
