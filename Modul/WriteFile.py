from pathlib import Path

class ReadWriteFile:
    def write_file(self, directory):
        name_file = directory['Surname']
        path_to_file = Path("repository", f"{name_file}.txt")
        try:
            with open(path_to_file, "a") as f:
                for value in directory.values():
                    f.write(f"<{value}>")
                f.write("\n")
        except FileNotFoundError:
            print("At the root of the project create a directore named 'repository'")
