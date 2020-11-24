from abc import ABC, abstractmethod
import os
import shutil

class Writer(ABC):
    def __init__(self):
        pass


    def init_directory(self, dir_path):
        # Remove directory if exists
        try:
            shutil.rmtree(dir_path)
        except OSError as e:
            print("Error: %s : %s" % (dir_path, e.strerror))

        # Create directory
        try:
            os.makedirs(dir_path)
        except OSError:
            print("Creation of the directory %s failed" % dir_path + "\n")
        else:
            print("Successfully created the directory %s" % dir_path + "\n")