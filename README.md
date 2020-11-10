[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
<br>
[![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-css.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-js.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-git.svg)](https://forthebadge.com)
<br>
## How To:
#### Execute the following in terminal:
<br>

```
mkdir AuditionForm
cd AuditionForm
sudo apt install python3-venv
python3 -m venv <environment name>
source <environment name>/bin/activate
git clone https://github.com/harshitsurana/audition-form-django.git
cd audition-form-django
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
<br>
Now the server is running at `127.0.0.1:8000`
<br>
Use the given database as it has some existing data to be used for state and cities

