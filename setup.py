from distutils.core import setup
import os

setup(name='Spion',
      version='1.0',
      description='Spies on and notifies for specified changes in webpages/websites.',
      author='Alexander Suraphel',
      author_email='alexsuraphel@gmail.com',
      license='Creative Commons Attribution-Noncommercial-Share Alike license',
      url='http://www.vnodeinfotech.com',
	  packages=['Spion'],
      #py_modules=['noti_db', 'noti_window', 'ReportFileCreator', 'crawler', 'Spion', '__init__'],
      package_data={'Spion':['README.txt', 'HOWTOUSE.txt', 'exec.bat'] }
      #data_files=[('Spion', ['README.txt', 'exec.bat'])]
     )

#schedule a task to check webpages repeatedly
os.system('schtasks /Create /SC HOURLY /TN Spion /TR "C:\Python26\Lib\site-packages\Spion\exec.bat"')