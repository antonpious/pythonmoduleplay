# pythonmoduleplay
Setting up internal modules in Python


Create a virtual environment from within VSCode  
`python3 -m venv venv`

Active the virtual environment  
`source venv/bin/activate`

Install the dependencies  
`pip install -r requirements.txt`


## Solution 1 - Have a Python Path
Create a python path to your module   
You can do this by editing the ~/.zshrc in mac os and adding this line  
`export PYTHONPATH=/Users/<user>/<projectparentdirectory>/`

Reload the terminal if already loaded using
`source ~/.zshrc` 

Note:  
Setting this variable in the .env file for python-dotenv did not work  



