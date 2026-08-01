# file operation
import os
import datetime


class fileOperator:

    reader_file, writer_file = '', ''

    def __init__(self, read, write):
        self.reader_file = read
        self.writer_file = write

    def file_exits(self):

        if os.path.exists(self.reader_file):
            print(f'>> Reader file located at {self.reader_file}')

            if os.path.exists(self.writer_file):
                print(f'>> Writer file located at {self.writer_file}')
            else:
                print(f'>> Writer file not avaialble in the located {self.writer_file}')
                with open(self.writer_file, 'x') as f2:
                    f2.close()
                print(f'>> Writer file created in the located {self.writer_file}')

            return True

        else:
            return False


    def file_writer(self):

        if self.file_exits():
            print('>> Data Appending operation from file1 to file2 is in progress.....')

            with open(self.reader_file) as f1:
                with open(self.writer_file, 'a') as f2:
                    for lines in f1.readlines():
                        f2.write(lines)
                    f2.write(f'\n-------------------------------------------------------------------------{
                             datetime.datetime.now()}\n')
                f2.close()
            f1.close()

            return 'Operation completed succesfully !!'

        else:
            return 'Error! Reader File doesnot exists. Kindly create in order to prcoceed.'


read = 'G:\\My Drive\\Project Docs\\Python\\file1.txt'
write = 'G:\\My Drive\\Project Docs\\Python\\file2.txt'
fileObject = fileOperator(read, write)
print(fileObject.file_writer())
