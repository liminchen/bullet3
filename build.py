import subprocess

runCommand = 'mkdir build\ncd build\ncmake -DCMAKE_BUILD_TYPE=Release ..\nmake -j 7'
subprocess.call([runCommand], shell=True)
