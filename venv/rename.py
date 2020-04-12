import os
import csv

class Renaming():
    """
        >>> tt = Renaming()
        >>> tt.get_path_csv('Test')
        >>> tt._path_csv
        'Test'
        >>> tt.get_path_csv(1)
        >>> tt._path_csv
        1
        >>> tt.get_path_csv(45)
        >>> tt._path_csv #doctest: +ELLIPSIS
        45
        >>> tt._get_csv()
        Traceback (most recent call last):
        OSError: ...
    """
    _path = ''
    _path_csv=''
    _path_renamed_dir = ''



    def get_path_csv(self, path_csv):
        '''
        >>> tt.get_path_csv('Test')
        >>> tt._path_csv
        'Test'
        '''
        self._path_csv = path_csv

    # Получение списка строк из файлов, где нулевой элемент имя файла, который нужно переименовать,
    # а первый элемент название, в которое нужно переименовать
    def _get_csv(self):
        with open(self._path_csv, "r", newline="") as file:
            list_str = dict(csv.reader(file, delimiter=';'))
        return list_str


    # Проверка существования пути к директории с файлами для переименовывания
    def get_path(self, path):

        if os.path.exists(path):
            self._path = path
            return True
        else:
            return False

    # Создание папки для переименованных файлов в той же директории
    def _create_renamed_dir(self):
        self._path_renamed_dir = os.path.join(self._path, 'renamed')
        try:
            os.mkdir(self._path_renamed_dir)
            msg = 'Директория rename была успешно создана'
        except FileExistsError:
            msg = 'Директория rename была создана ранее. Данная директория должна быть пустой, проверьте отсутствие в ней файлов!'
        return msg

    def rename(self):
        # Соловарь переименований
        dict_name = self._get_csv()
        # Список файлов в директории
        files = os.listdir(self._path)
        self._create_renamed_dir()
        for f in files:
            src_parh = os.path.join(self._path, f)
            if os.path.isfile(src_parh):
                name_file = f.split('.')[0]
                r_name = dict_name.get(name_file)
                if r_name:
                    r_name = r_name + ".pdf"
                    os.rename(src_parh, os.path.join(self._path_renamed_dir, r_name))


#--------- for tests -------------------
def create_env_for_tests():
    dir_for_files = os.path.join(os.getcwd(), 'test', 'files')
    os.mkdir(dir_for_files)
    #os.chdir(dir_for_files)
    for i in range(1, 10):
        pdf_file = open(os.path.join(dir_for_files, f"{i}.pdf"), "w")
        pdf_file.close()

def del_env_for_tests():
    dir_for_files = os.path.join(os.getcwd(), 'test', 'files')
    for i in range(1, 10):
        del_path = os.path.join(dir_for_files, f'{i}.pdf')
        os.remove(del_path)
    os.rmdir(dir_for_files)
#--------- end tests ------------------

if __name__ == '__main__':
    import doctest
    # create_env_for_tests()
    doctest.testmod(optionflags=+doctest.ELLIPSIS, globs={'tt':Renaming()})

