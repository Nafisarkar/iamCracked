def main():
    """
    This function will execute every code inside the modules folder.
    The modules folder contains some python scripts with py extension.
    The main function is just execute all the python scripts available on the modules folder one by one.
    """
    import glob
    import os
    import subprocess

    # Get all the python scripts in the modules folder
    files = glob.glob(os.path.join('iamCracked/modules', '*.py'))
    
    # Print all the files that found in the folder
    print("Files that found in the folder:")
    for file in files:
        print(file)

    # Execute all the python scripts one by one
    for file in files:
        subprocess.call(['python', file])


if __name__ == '__main__':
    main()
