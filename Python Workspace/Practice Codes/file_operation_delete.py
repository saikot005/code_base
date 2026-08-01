import os


def file_delete(file_path):

    if os.path.exists(file_path):
        os.remove(file_path)
        print('File deleted')
    else:
        print('file not found')


file_delete('G:\\My Drive\\SourceCodes\\Python\\Python_DE\\file3.txt')    