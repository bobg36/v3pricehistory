import shutil
import os
import subprocess
import sys


# print('generating data')
# subprocess.run(['python', 'generate all charts.py'], cwd='C:\\Users\\bobgu\\Desktop\\record all sales july 2023\\axie sql')


print('copying charts to local folder')
source_dir = r'C:\Users\bobgu\Desktop\record all sales july 2023\axie sql\flask\static'
destination_dir = os.getcwd() + '//data'
if os.path.exists(destination_dir):
    shutil.rmtree(destination_dir)
    print('data deleted')
shutil.copytree(source_dir, destination_dir)
print(f'Copied contents of "{source_dir}" to current working directory "{destination_dir}"')


print('generating html')
script_path = 'generatehtml.py'
subprocess.run(['python', script_path], check=True)



print('pushing data updates to github. website should be live in 40 seconds')
git_add = 'git add .'
git_commit = 'git commit -m "data update"'
git_push = 'git push origin main'
subprocess.run(git_add, shell=True)
subprocess.run(git_commit, shell=True)
subprocess.run(git_push, shell=True)