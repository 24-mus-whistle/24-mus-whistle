import os

def load_data(data_dir: str) -> list[str]:
    """
    Determine absolute paths of all files located in passed `data_dir`.

    Args:
        data_dir (str): absolute path to directory in which the data is stored

    Returns:
        list[str]: List of absolute paths of all files in passed `data_dir`
    """
    paths = map(
        lambda file: os.path.normpath(os.path.join(data_dir, file)),
        os.listdir(data_dir)
    )
    
    # keep only csv and flac
    data_file_paths = []
    for file in paths:
        extension = os.path.splitext(file)[1]
        if extension != '.flac' and extension != '.csv':
            continue
        else:
            data_file_paths.append(file)
    
    data_file_paths = list(data_file_paths)
    return data_file_paths
