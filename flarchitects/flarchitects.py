"""
-- Flarchitect Project --

Dynamic creator for static, view and html files.

Zachary Spar <zachspar@gmail.com>

"""
import sys


_type_ = sys.argv[1]
app_name = sys.argv[2]

type_name = str()
source_file = str()
file_path = str()

if _type_ == 'view':
    type_name = sys.argv[3]
    source_file = 'flarchitects/view.py'
    file_path = app_name + '/' + app_name + '/views/' + type_name + '.py'
    print(type_name)
elif _type_ == 'template':
    template_name = sys.argv[3]
    source_file = 'flarchitects/template.html'
    file_path = app_name + '/' + app_name + '/templates/' + template_name + '.html'
elif _type_ == 'init':
    source_file = 'flarchitects/init_file.py'
    file_path = app_name + '/' + app_name + '/__init__.py'
elif _type_ == 'config':
    source_file = 'flarchitects/config_file.py'
    file_path = app_name + '/' + app_name + '/config.py'
elif _type_ == 'setup':
    source_file = 'flarchitects/setup_file.py'
    file_path = app_name + '/setup.py'
elif _type_ == 'bin':
    source_file = 'flarchitects/run_app_script'
    file_path = app_name + '/bin/run_server'

with open(source_file, 'r') as infile, open(file_path, 'wb') as outfile:
    for line in infile:
        if 'view_name' in line:
            line = line.replace('view_name', type_name)
        if 'app_name' in line:
            line = line.replace('app_name', app_name)
        outfile.write(line.encode('utf-8'))
    outfile.close()
    infile.close()
