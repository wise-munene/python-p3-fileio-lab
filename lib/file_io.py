def write_file(file_name, file_content):
    path= f"{file_name}.txt"
    with open (path,'w') as file:
        file.write(file_content)




def append_file(file_name, append_content):
    path=f"{file_name}.txt"
    with open (path, "a") as file:
        file.write(append_content)

def read_file(file_name):
    path=f"{file_name}.txt"
    with open(path, "r") as file:
        return file.read()
