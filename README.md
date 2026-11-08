# REVOLT Bike Showroom — Django project

A responsive bike showroom website built with Django, HTML and CSS. It includes bike listings, search/filter, bike detail pages, a contact form, and Django admin.

## Requirements
- Python 3.10 or newer
- VS Code with Python extension recommended
- Internet connection for the sample remote bike images

## Run on Windows (VS Code)

1. Extract this ZIP and open the `bike_showroom` folder in VS Code.
2. Open **Terminal → New Terminal**.
3. Create a virtual environment:

   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt and run `.venv\Scripts\activate.bat`, or run `py -m pip install -r requirements.txt` without activating the environment.

4. Install Django:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Create database tables:

   ```powershell
   python manage.py makemigrations bikes
   python manage.py migrate
   ```

6. Add sample bikes:

   ```powershell
   python manage.py seed_bikes
   ```

7. Start the local development server:

   ```powershell
   python manage.py runserver
   ```

8. Open http://127.0.0.1:8000/ in your browser.

## Admin panel
Create an admin account:

```powershell
python manage.py createsuperuser
```

Then visit http://127.0.0.1:8000/admin/ and sign in to add/edit bikes or read contact messages.

## Pages
- `/` — Home
- `/bikes/` — Bike collection, search and category filter
- `/bikes/1/` — Example bike detail (the ID depends on your database)
- `/contact/` — Contact form
- `/admin/` — Django admin

## Notes
- Sample brands, model names and prices are fictional demo data; update them before using the site commercially.
- Bike images load from remote Unsplash URLs, so an internet connection is needed to display them.
- `DEBUG=True` and the included secret key are for local development only. Do not deploy this configuration publicly.
