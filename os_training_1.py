import os


def current_path():
    # to get current working directory
    print("current working dir", cwd := os.getcwd())
    return cwd


def change_directory(dir):
    os.chdir(dir)
    current_path()


# change_directory('../')

def create_directory(dir):
    not_created_yet_dir = os.path.join(current_path(), dir)
    if not os.path.exists(not_created_yet_dir):
        os.mkdir(not_created_yet_dir)
    change_directory(not_created_yet_dir)


create_directory('training_creating_directories')

print(os.name)
