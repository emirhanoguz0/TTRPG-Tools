import glob

def taking_file_paths(dizin):
    file_paths = glob.glob(f"{dizin}/*")
    return file_paths