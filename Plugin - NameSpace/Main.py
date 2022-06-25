from PluginExt import *

class ExtensionClass:
    __map = {}
    def __init__(self, directories:list) -> None:
        add_paths(directories)
        self.__map = get_plugins("extension")
    def invoke_method(self, key:str) -> None:
        try:
            use_plugin(self.__map, key, "method")
        except:
            raise KeyError(f"There aren't any extension modules with Key: {key}")

Object = ExtensionClass([".\path1\src\\",".\path2\src\\"])
Object.invoke_method("One")
Object.invoke_method("Two")