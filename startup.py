import os
SCRIPT_LOCATION = '/manage.py'

def execute_startup_script():
    startup = 'python .'+SCRIPT_LOCATION+' runserver'
    os.system(startup)

execute_startup_script()