import os


def find_requirements_txt_files(root_directory):
    requirements_files = []

    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith('.txt') and file.startswith('requirements'):
                rel_path = os.path.relpath(
                    os.path.join(root, file), root_directory,
                )
                requirements_files.append(rel_path)

    print('requirements', requirements_files)

    return requirements_files


def find_driver_scripts(path, ignore_dirs=None):
    if ignore_dirs is None:
        ignore_dirs = []

    ignore_dirs += ['venv', '.venv']

    driver_codes = []
    for root, dirs, files in os.walk(path):
        ignore = False
        x = os.path.relpath(root, path)

        for i in ignore_dirs:
            if i in x:
                ignore = True

        if ignore:
            continue

        for file in files:
            if file.endswith('.ipynb') or file.endswith('.py'):
                rel_path = os.path.relpath(os.path.join(root, file), path)
                driver_codes.append(rel_path)
                # notebooks.append(os.path.join(root, file))
    return driver_codes
