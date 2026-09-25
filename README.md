# Suyog Bhandari Portfolio

A Django and vanilla JavaScript developer portfolio for Suyog Bhandari.

## Local setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser.

## Configuration

Copy `.env.example` to `.env` and provide deployment-specific values. The project uses SQLite locally and Django's console email backend by default, so the contact form works without email credentials. Set `CONTACT_EMAIL` and SMTP environment variables when a real inbox is ready.

Social URLs and portfolio content are centralized in `portfolio/views.py`. Replace the placeholder GitHub and LinkedIn URLs there before publishing.

## Vercel deployment

Vercel detects this Django project from `manage.py` and `WSGI_APPLICATION`. No custom `vercel.json` is required.

1. Import the GitHub repository into Vercel.
2. Use the repository root as the project root and keep the detected Django/Python framework setting.
3. Add these Production environment variables:

	- `DJANGO_SECRET_KEY`: a long random secret
	- `DJANGO_DEBUG`: `False`
	- `DJANGO_ALLOWED_HOSTS`: your Vercel hostname, such as `your-project.vercel.app`
	- `DJANGO_CSRF_TRUSTED_ORIGINS`: your HTTPS Vercel URL, such as `https://your-project.vercel.app`
	- `EMAIL_BACKEND`: `django.core.mail.backends.smtp.EmailBackend`
	- `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_USE_TLS`
	- `DEFAULT_FROM_EMAIL` and `CONTACT_EMAIL`

The portfolio has no application models, so its static project content does not require a persistent database. Vercel's filesystem is ephemeral; use an external database before adding persistent application data.
