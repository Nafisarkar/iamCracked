import os
import importlib.util

def main():
    # Specify the directory where your module scripts are located
    module_directory = "modules"

    # Get a list of all Python files in the module directory
    module_files = [f for f in os.listdir(module_directory) if f.endswith(".py")]

    # Iterate over each module file and execute it
    for module_file in module_files:
        module_path = os.path.join(module_directory, module_file)
        
        # Load the module dynamically using its file path
        spec = importlib.util.spec_from_file_location(module_file, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Call the main function of the module (assuming it has one)
        if hasattr(module, "main"):
            module.main()

if __name__ == "__main__":
    main()