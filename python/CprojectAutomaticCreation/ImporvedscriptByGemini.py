import os
import shutil

def create_project_structure(project_name):
    os.system(f"mkdir -p {project_name}/src")
    os.system(f"mkdir -p {project_name}/tests")
    os.system(f"mkdir -p {project_name}/build")

def create_main_file(project_name):
    with open(f"{project_name}/src/main.cpp", "w") as file:
        file.write("""#include <iostream>

           int main() {
             std::cout << "Hello From the Automatic Script";
               return 0;
           }
           """)

def create_cmake_file(project_name, cmake_version):
    with open(f"{project_name}/CMakeLists.txt", "w") as file:
        file.write(f"""cmake_minimum_required(VERSION {cmake_version})

         project({project_name})
         include_directories(src)
         add_executable({project_name} src/main.cpp)
         """)

def build_project(project_name):
    os.chdir(f"{project_name}/build")
    os.system("cmake .. && make -j && ./helloWorld")

if __name__ == "__main__":
    project_name = input("Enter project name: ")
    cmake_version = input("Enter minimum required CMake version (e.g., 3.10): ")

    if os.path.exists(project_name):
        shutil.rmtree(project_name)
        print(f"The project folder '{project_name}' was found and removed.")

    create_project_structure(project_name)
    create_main_file(project_name)
    create_cmake_file(project_name, cmake_version)
    build_project(project_name)

    print(f"\nBuilding the project '{project_name}' is done.")
