#1
import os
path = r'C:\Users\user\Desktop\pp2'
directories_list = os.listdir(path)
print("Files and directories in' ", path, "':")
print(directories_list)
#2
import os
path = r'C:\Users\user\Desktop\pp2'
def check_path_(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return
    if os.access(path, os.R_OK):
        print(f"Read access to '{path}' is allowed.")
    else:
        print(f"No read access to '{path}'.")
    if os.access(path, os.W_OK):
        print(f"Write access to '{path}' is allowed.")
    else:
        print(f"No write access to '{path}'.")
    if os.access(path, os.X_OK):
        print(f"Execute access to '{path}' is allowed.")
    else:
        print(f"No execute access to '{path}'.")
if __name__ == "__main__":
    path_to_check = input("Enter the path to check: ")
    check_path_(path_to_check)
#3
import os
path = r'C:\Users\user\Desktop\pp2'
def ana_path(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    print(f"Path '{path}' exists.")
    print(f"Filename: {filename}")
    print(f"Directory: {directory}")
if __name__ == "__main__":
    path_to_analyze = input("Enter the path to analyze: ")
    ana_path(path_to_analyze)

#4
def count_l(path):
    try:
        with open(path, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"The number of lines in the file '{path}' is: {line_count}")
    except FileNotFoundError:
        print(f"The file '{path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    file_path = input("Enter the path of the text file: ")
    count_l(path)

#5
def write_list_to(path, my_list):
    try:
        with open(path, 'w') as file:
            for item in my_list:
                file.write(str(item) + '\n')
        print(f"The list has been successfully written to the file '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    path = input("Enter the path and filename to write the list to: ")
    sample_list = ['item1', 'item2', 'item3', 'item4']
    write_list_to(path, sample_list)

#6
import os
path = r'C:\Users\user\Desktop\pp2'
def generate_text():
    try:
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            path = f"{letter}.txt"
            with open(path, 'w') as file:
                file.write(f"This is the content of file {path}")
        print("Text files generated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_text()


#7
import os
path = r'C:\Users\user\Desktop\pp2'
def copy_file(path, destination_path):
    try:
        with open(path, 'r') as source_file:
            content = source_file.read()

        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)

        print(f"Contents of '{path}' successfully copied to '{destination_path}'.")
    except FileNotFoundError:
        print(f"Error: One of the files does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    # Replace 'source.txt' and 'destination.txt' with the actual file paths
    path = input("Enter the source file path: ")
    destination_path = input("Enter the destination file path: ")

    copy_file(path, destination_path)



#8
import os
path = r'C:\Users\user\Desktop\pp2'
def delete_fi(path):
    try:
        if not os.path.exists(path):
            print(f"The file '{path}' does not exist.")
            return
        if not os.access(path, os.W_OK):
            print(f"No write access to '{path}'. Cannot delete.")
            return
        os.remove(path)
        print(f"The file '{path}' has been successfully deleted.")
    except FileNotFoundError:
        print(f"The file '{path}' does not exist.")
    except PermissionError:
        print(f"No permission to delete '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    file_path_to_del = input("Enter the path of the file to delete: ")
    delete_fi(file_path_to_del)

