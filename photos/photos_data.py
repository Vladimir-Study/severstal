import os 
import pathlib


class Photo():

    def file_size(self, file_path):
        stats = os.stat(file_path)
        return stats.st_size

if __name__ == "__main__":
    pass