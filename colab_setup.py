import os

os.rmdir("energyplus")
os.system("git clone https://github.com/energy-plus-senior-design/eplusparser.git")
os.chdir("eplusparser")
os.system("pip install .")
