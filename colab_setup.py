from google.colab import drive

drive.mount('/content/drive')

!rm -rf eplusparser && git clone https://github.com/energy-plus-senior-design/eplusparser.git

%cd eplusparser
!pwd
!pip install .
