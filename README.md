# Python project boiler plate

## How to Setup

 - Make a copy/fork of this repository
 - Update the following values in setup.py:
   - name
   - version
   - description
   - author
   - license
   - classifiers
   - install requires
   - extras_require
 - Update the docker file:
   - add your contact info to the `MAINTAINER` line
   - `CMD` to whatever command starts your app
 - In OneDev edit the `.onedev-buildspec.yaml` file:
   - edit step templates:
     - update execute tests to run your test suite(s) if not pytest
     - 


----

# Beryl
named after the rare gemstone: https://en.wikipedia.org/wiki/Beryl


## Local Setup

### Install Miniconda

For installers for operating systems other than linux see https://docs.conda.io/en/latest/miniconda.html

    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -s --output miniconda.sh
    chmod +x miniconda.sh
    ./miniconda.sh -u
    rm miniconda.sh

### Create conda enviroment

You may need to reopen your shell after installing miniconda

    conda create -n beryl python=3.10
    conda activate beryl
    conda install --file requirements.txt

### Run the project

The default port is 5000

    python ./app/main.py

## Docker

### Building the Docker container

With your working directory in the root of the repository

    docker build --tag beryl .

### Running the Docker container

    docker run -p 5000:5000 beryl

or for detached mode

    docker run -d -p 5000:5000 beryl    


### Publishing to docker

    docker login
    docker build --tag mullinmax/beryl:latest .
    docker push mullinmax/beryl:latest
