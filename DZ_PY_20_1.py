import os, os.path, time
#     * * * * *     * * * * *     * * * * *     1

# file = r'text_dir\f1\4.txt'
file = r'C:\Users\Stani\...\DZ_PY_1.py'
if os.path.exists(file):
    print(os.path.basename(file))
    print(os.path.dirname(file))
    print(os.path.getatime(file))
else:
    print('Файл не существует')

#     * * * * *     * * * * *     * * * * *     2

dir_name = 'files'
file = []
dirs = []
search = os.listdir(dir_name)
print(search)
for i in search:
    mp = os.path.join(dir_name, i)
    if os.path.isfile(mp):
        file.append(dir_name + '//' + i)
    elif os.path.isdir(mp):
        dirs.append(dir_name + '//' + i)
end = file + dirs
print(end)

#     * * * * *     * * * * *     * * * * *     2

os.makedirs('Work\empty_files')
for root, files in os.walk('Work'):
    for i in files:
        mp = os.path.join(root, i)
        if os.path.getsize(mp) > 0:
            print(f'{root}\\{i}-{os.path.getsize(mp)} bytes')
        else:
            gen = os.path.basename(i)
            os.replace(mp, f'Work\empty_files\{gen}')
