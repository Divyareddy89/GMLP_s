from setuptools import setup,find_packages
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
   name='GMLP_s',
   version='0.0.1',
   description='First ML project',
   author='Divyareddy89',
   author_email='divreddy89.78@gmail.com',
   packages=find_packages(),
   install_requires=['requirements.txt']
)