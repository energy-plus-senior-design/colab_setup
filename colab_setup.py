import os
from google.colab import drive

drive.mount('/content/drive')

os.system("rm -rf eplusparser && git clone https://github.com/energy-plus-senior-design/eplusparser.git")

os.system("cd eplusparser")
os.system("pwd")
os.system("pip install .")
