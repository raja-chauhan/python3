"""
Virtual enviorment allow your every single project to make it's own configuration without affecting other project configuration on a single pc.

In order to use it you have to install package --> pip install virtualenv

> sudo virtualenv harryenv 
# it will create new virtual env (new clone of python3 )

> ./harryenv
>./harry/scripts/activate
#  activate the enviorment

In ubuntu
python3 -m venv my-project-env

Activate -> source harryenv/bin/activate


once the envioemnt becaome active you can start installing packages which you want to use
eg. pip install sklearn

*******  pip freeze > requirment.txt # to auto generate requirment file
pip install -r ./requirment.txt

to install any module of specific version 
> pip install module --version



To deactivate virtualenv

> deactivate


========================================================================================
latest commands for ubuntu

install pip
apt install python3-distutils
pip --version
pip install virtualenv
create new virtual enviorment
> virtualenv -p python3 myenv
source myenv/bin/activate
pip install package_name
deactivate

"""