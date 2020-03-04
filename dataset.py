import os

class Dataset:
    def __init__(self, directory):
        self.root_directory = directory

    def walk(self):
        paths = []
        if os.path.isdir(self.root_directory):
            for root, dirs, files in os.walk(self.root_directory):
                for file_name in files:
                    path = os.path.join(root, file_name)
                    paths.append(path)
        else:    
            paths.append(self.root_directory)

        for path in paths:
            print(path)
            with open(path, 'r', encoding = "utf8") as f:
                for line in f:
                    yield line
