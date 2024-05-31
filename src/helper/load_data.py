import os

def load_data(data_dir: str) -> list[str]:
    """
    Determine absolute paths of all files located in passed `data_dir`.

    Args:
        data_dir (str): absolute path to directory in which the data is stored

    Returns:
        list[str]: List of absolute paths of all files in passed `data_dir`
    """
    data_file_paths = map(
        lambda file: os.path.normpath(os.path.join(data_dir, file)),
        os.listdir(data_dir)
    )
    data_file_paths = list(data_file_paths)
    return data_file_paths
