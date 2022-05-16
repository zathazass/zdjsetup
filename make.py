'''Command-Line Utility for updating project as yours'''

import os, sys
from pathlib import Path

def get_data():
	# Getting required information from developer
	proj_name = input('Enter Your Project Name : ')

	# Checking value with constraints
	if not proj_name.isidentifier():
		print('Project Name must be an pythonic identifier format')
		sys.exit()

	return {'proj_name': proj_name}


# Setting up our replace str (old value in "key", new value in "value")
def prepare_replace_map(data):
	return {
		'project_name': data.get('proj_name').strip()
	}

# Getting current directory details
def get_ls_details(_dir):
	dir_list = [fd for fd in os.scandir(_dir) if fd.is_dir()]
	file_list = [fd for fd in os.scandir(_dir) if fd.is_file()]
	return dir_list, file_list

# Replacing string one by one on every file
def replace_str(_dir=None, replace_map=None):
	replace_map = replace_map or {}
	_dir = _dir or '.'
	dir_list, file_list = get_ls_details(_dir)
	
	for _file in file_list:
		for key, value in replace_map.items():
			file = Path(f'{_dir}/{_file.name}')
			file.write_text(file.read_text(encoding='utf-8').replace(f'<<{key}>>', value))		
						
	for dir_ in dir_list:
		replace_str(f'{_dir}/{dir_.name}', replace_map)					


if __name__ == '__main__':
	data = get_data()
	os.rename('project_dir', data.get('proj_name'))
	replace_str('.', prepare_replace_map(data))
	

	
	
	
