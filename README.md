# LoadTestUrsus
Locust script to load test ursus.library.ucla.edu

Steps to install python 
https://docs.python-guide.org/starting/install3/linux/

Locust
Install python3 for locustio

Instructions to install locust are here: https://docs.locust.io/en/stable/installation.html

Docs for locustio:  https://docs.locust.io/en/stable/quickstart.html

On Mac OSX I followed the instructions below:

1. Install python using pyenv
  Good resource https://www.freecodecamp.org/news/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f/

2. create a virtual environment to run python
 pyenv virtualenv 3.6.0 my-virtual-env-3.6.0
 
3. clone this repo

4. cd LoadTestUrsus

5. brew install pyenv-virtualenv
   pyenev virtualenvs
   pyenv virtualenv 3.6.0 my-virtual-env-3.6.0

6. Activate virtual env

7. pyenv activate my-virtual-env-3.6.0

8. pip install locust

9. Run the locust script from this repo

10. locust -f locust_ursus.py --host http://ursus.library.ucla.edu
