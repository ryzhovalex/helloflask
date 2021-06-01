# helloflask

Flask template to start developing.

To launch on Linux:
```bash
    $ cd <this_project_directory>
    $ export FLASK_APP=core
    $ flask run
```

To launch on Windows:
cmd:
```cmd
    > set FLASK_APP=core
    > flask run
```
powershell:
```powershell
    > $env:FLASK_APP = "core"
    > flask run
```

**Important:** If you are launching for the first time, before running 'flask run' and after setting 'FLASK_APP', you should create a database, by typing following commands (same for both Windows and Linux):
```bash
    $ flask db init
    $ flask db migrate
    $ flask db upgrade
```
