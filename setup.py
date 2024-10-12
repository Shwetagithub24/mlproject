from setuptools import find_packages,setup   #find all the packages in dir we created
from typing import List

HYPEN_E_DOT='-e .'  

'''this function will return list of all the requirements'''
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
         requirements=file_obj.readlines()
         requirements=[req.replace("\n","")for req in requirements]

         if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

#metadata of entire project
setup (
    name="mlproject",
    version="0.0.1",
    author="Shwetanjali",
    author_email="shwetazarekar6@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

"""
how it will find out how many packages are there?
Src folder  create __init__.py  
When find_packages() functions runs in setup.py will will go and search in how many folders we have constructor file.
"""

