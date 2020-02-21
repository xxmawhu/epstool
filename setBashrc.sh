#source bash_alias.sh 
pwd=$(pwd)
if [ "$(grep "epstool/setup" ~/.bashrc)" == "" ] 
then
    echo "source $pwd/setup.sh" >> ~/.bashrc
fi
