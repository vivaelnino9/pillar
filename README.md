# pillar
Pillar - Take Home Exercise (GitHub)


Setting up Environment:

- Clone/download the repo
- Create a [virtualenv](https://virtualcnv.pypa.io/en/latest/) inside the repo with `virtualenv env --python=python3`
- Activate the env with `source env/bin/activate` 
- Install requirements with `pip install -r requirements.txt`

Running:

- In one tab, first migrate with `./manage.py migrate`
- Then run `./manage.py runserver`

- In another tab `cd` into `frontend`
- Run `ng serve`
- The app should now be avaiable locally at `http://localhost:4200/organizations`


Side-Note:
Unfortunately as of now the create organization component on the frontend is not working so a workaround in order to create new organizations is to visit the actual [Django REST UI page](http://127.0.0.1:8000/organizations) and create an organization using the form at the bottom.
