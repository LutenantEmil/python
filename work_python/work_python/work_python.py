import psutil
import os


def File_sistem_cur_dir ():
    return os.getcwd()

def File_sistem_dir_list():
    return os.listdir(os.getcwd())


def kommand_execute(command):
    os.system(command)

def proc_list():
    a= [];
    for p in psutil.process_iter():
        a.append(p)
    return a



#пример к выполнению команды по определению текущей дирректории
"""
direkt = File_sistem_cur_dir()
print(direkt)
"""

#пример к выполнению команды по просмотру находящегося в текущей директории
"""
i = 0
direkt = File_sistem_dir_list()
while i < len(direkt):
    print (direkt[i])
    i = i+1
"""

#пример к выполнению консольных комманд
"""
command = "help"
kommand_execute(command)
"""


# пример выполнения получения списка процессов
"""
c = proc_list()
i = 0
while i < len(c):
    print (c[i])
    i = i+1
"""
