import os
import shutil
from google.colab import drive

drive.mount('/content/drive')

shutil.rmtree("eplusparser", ignore_errors=True)
os.system("git clone https://github.com/energy-plus-senior-design/eplusparser.git")

os.chdir("eplusparser")
os.system("pip install .")
