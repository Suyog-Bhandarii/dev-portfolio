from django.conf import settings
from django.contrib import messages
from django.core.mail import mail_admins, send_mail
from django.shortcuts import redirect, render

from .forms import ContactForm


PORTFOLIO_OWNER = {
	'name': 'Suyog Bhandari',
	'role': 'BIT Student • Aspiring Full-Stack Developer',
	'education': 'Bachelor of Information Technology',
	'institution': 'Texas College of Management & IT, Kathmandu',
	'location': 'Kathmandu, Nepal',
	'email': 'suyogbhandari93@gmail.com',
	'github': 'https://github.com/Suyog-Bhandarii',
	'linkedin': 'https://www.linkedin.com/in/suyog-bhandari06/',
}

PROJECTS = [
	{
		'title': 'PaisaWallet',
		'category': 'Digital Wallet / Financial Simulation',
		'description': 'A simulated digital wallet and payment platform built with Flask and SQLAlchemy, featuring wallet balances, peer-to-peer transfers, transaction history, merchant payments, and financial transaction safeguards.',
		'context': 'Educational / simulated payment system',
		'tags': ['Python', 'Flask', 'SQLAlchemy', 'PostgreSQL', 'HTML', 'CSS', 'JavaScript'],
		'github': 'https://github.com/Suyog-Bhandarii/PaisaWallet',
		'demo': '',
		'class': 'project-pet',
		'icon': 'wallet-cards',
	},
	{
		'title': 'Complaint Management System',
		'category': 'Django Web Application',
		'description': 'A web-based complaint management system designed to allow complaints to be submitted, managed, tracked, and organized through a structured web interface.',
		'tags': ['Python', 'Django', 'Django REST Framework', 'HTML', 'CSS', 'JavaScript', 'Database'],
		'github': 'https://github.com/Suyog-Bhandarii/Complaint-Management-System',
		'demo': 'https://complaintmanagementsystem-nu.vercel.app/',
		'class': 'project-system',
		'icon': 'clipboard-list',
	},
	{
		'title': 'MovieVerse',
		'category': 'React Web Application',
		'description': 'A React-based movie discovery application for exploring trending and currently playing movies, searching the TMDB catalog, filtering by genre, viewing movie details, and managing a personal watchlist.',
		'context': 'Demo authentication uses browser localStorage.',
		'tags': ['React', 'Vite', 'React Router', 'JavaScript', 'CSS', 'TMDB API'],
		'github': 'https://github.com/Suyog-Bhandarii/MovieVerse',
		'demo': 'https://movie-verse-two-azure.vercel.app/',
		'class': 'project-todo',
		'icon': 'clapperboard',
	},
	{
		'title': 'JobMandu',
		'category': 'Web Application / Job Portal',
		'description': 'A web-based job portal built for a Web Technology project, allowing users to explore and manage job-related information through a structured web application.',
		'context': 'Web Technology (BIT-233)',
		'tags': ['Python', 'Flask', 'MySQL', 'HTML', 'CSS', 'Bootstrap 5'],
		'github': 'https://github.com/Suyog-Bhandarii/jobmandu',
		'demo': '',
		'class': 'project-portfolio',
		'icon': 'briefcase-business',
	},
]


SKILLS = {
	'current': ['Python', 'Django', 'Flask', 'JavaScript', 'HTML', 'CSS', 'SQL', 'Git', 'GitHub'],
	'exploring': ['React', 'Django REST Framework', 'PostgreSQL', 'APIs', 'Deployment', 'AI-assisted development'],
	'academic': ['Java', 'Object-Oriented Programming', 'Database Management', 'Operating Systems', 'System Analysis & Design'],
}


def home(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			message = form.cleaned_data['message']
			subject = f"Portfolio message from {form.cleaned_data['name']}"
			body = f"From: {form.cleaned_data['email']}\n\n{message}"
			if settings.CONTACT_EMAIL:
				send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
			else:
				mail_admins(subject, body, fail_silently=True)
			messages.success(request, 'Thanks for reaching out. Your message is on its way.')
			return redirect('portfolio:home')
	else:
		form = ContactForm()

	return render(request, 'portfolio/home.html', {
		'owner': PORTFOLIO_OWNER,
		'projects': PROJECTS,
		'skills': SKILLS,
		'contact_form': form,
	})

# Create your views here.
