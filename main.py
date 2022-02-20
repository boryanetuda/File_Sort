import os


def txt_file_find():
    BASE = os.getcwd()
    files = os.listdir(BASE)
    txt = filter(lambda x: x.endswith('.txt'), files)
    worklist = list(txt)
    return worklist


def sort_files(worklist):
    len_txt = {}
    for i in range(len(worklist)):
        with open(worklist[i]) as f:
            len_txt[worklist[i]] = len(f.readlines())
    temp = sorted(len_txt.items(), key=lambda item: item[1])
    sorted_len_txt = {k: v for k, v in temp}
    val = list(sorted_len_txt.values())
    sorted_temp = []
    for k, v in sorted_len_txt.items():
        sorted_temp.append(k)
    sorted_txt = []
    for i in range(len(sorted_temp)):
        with open(sorted_temp[i]) as file:
            sorted_txt.append(file.readlines())
    BASE = os.getcwd()
    dir_name = 'temp'
    file_name = 'sorted.txt'
    sort_path = os.path.join(BASE, dir_name, file_name)
    with open(sort_path, 'w') as text:
        for i in range(len(sorted_txt)):
            text.write(f'{sorted_temp[i]}\n{val[i]}\n{"".join(sorted_txt[i])}\n')
    with open(sort_path) as t:
        print(t.read())


sort_files(txt_file_find())