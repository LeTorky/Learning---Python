from sys import path
from os import listdir
from importlib import import_module

def import_extension_modules(directories:list)->dict:
    """
    A recursive function that iterates through the given list of directories
    and searches for module files to import, then iterates through
    sub-directories if found to repeat the process.
    """
    imported_modules = {}
    search_directories = []
    for directory in directories:
        nested_directories = listdir(directory)
        directory_name = directory.replace("\\.\\","\\\\")
        path.append(f"{directory_name}")
        for child_directory in nested_directories:
            if child_directory.__contains__(".py") and not child_directory.__contains__('__init__.py'):
                module_name = child_directory.replace(".py","")
                module = import_module(module_name)
                imported_modules.update({module.key:module})
            elif not child_directory.__contains__('__pycache__') and not child_directory.__contains__('__init__.py'):
                search_directories.append(f"{directory}\{child_directory}")
        path.pop()
        imported_modules.update(import_extension_modules(search_directories))
    return imported_modules


def get_plugins(name_space:str)->dict:
    """
    A function that returns a dictionary of imported modules within a namespace,
    given that the directories are already appended to the systems path; it is
    fascilitated via the import_extension_modules method.
    """

    extension_module = import_module(name_space)
    return import_extension_modules(extension_module.__path__)

def add_paths(directories:list):
    """
    A function that appends paths into the system's path variable.
    """
    global path
    path.extend(directories)

def use_plugin(map:dict, key:str, method:str):
    """
    A function that uses a specific method within a specific module within
    a dictionary of modules, given the key of the module to invoke from.
    """
    getattr(map[key], method)()
