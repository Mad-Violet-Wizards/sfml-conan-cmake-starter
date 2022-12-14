import os
import shutil

def run():

    if (os.path.exists("build") == False):
        os.mkdir("build")
    
    os.chdir("build")
    os.system("cmd /c conan install .. --build missing")
    os.system(f'cmd /c cmake -G "Visual Studio 17 2022" ..')
    os.system('cmd /c cmake --build . --config Release')
    os.system('cmd /c conan imports ..')


if __name__ == "__main__":
    run()