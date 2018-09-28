1. `git clone git@github.com:CoworkerOrg/actionkit-templates.git`
1. `cd actionkit-templates`
1. `virtualenv --python=/usr/bin/python2.7 venv`
1. `source venv/bin/activate`
1. `pip install -r requirements.txt` (`pip freeze > requirements.txt` to overwrite with new dependencies)
1. `cd actionkit_project`
1. `python manage.py runserver`
2. Navigate to `localhost:8000/actionkit/` for the renderer homepage, which lists all the contexts that have been loaded and links to the pages where they'd be used

By default, templates are served out of `actionkit_project/templates/`. You can serve a different template set by putting a directory full of templates in the project root directory and pointing to the directory with the TEMPLATE_DIR environment variable. For example, if our new template directory is called test_templates, its path would be: `actionkit_project/test_templates/` and we'd run `TEMPLATE_DIR=test_templates python manage.py runserver`
