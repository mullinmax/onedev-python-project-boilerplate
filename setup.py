from setuptools import setup, find_packages

setup(
    name='Project Name',  # name of your project
    version='0.0.1',  # version number of your project
    packages=find_packages(),  # packages to include in your project
    include_package_data=True,  # include non-Python files in your package
    description='A brief description of your project',  # brief description of your project
    author='Maxwell Mullin',  # author of your project
    author_email='mullinmax@gmail.com',  # author's email address
    python_requires='>=3.6',  # minimum required version of Python for your project
    install_requires=[  # packages required to run your project
        'pytest'
    ],
    extras_require={  # optional dependencies for building or testing your project
        'build': [
            # dependencies required for building your package
        ],
        'test': [
            # dependencies required for testing your package
            'pytest'
        ],
    },
)
