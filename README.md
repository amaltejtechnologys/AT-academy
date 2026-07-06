# AT Academy — Full-Stack Django Website

A fully-featured, production-deployed educational institution website built with Django. Complete admin panel, dynamic content management, responsive design, and live deployment on PythonAnywhere.

**Live Site:** [https://AbdulAyaan.pythonanywhere.com](https://AbdulAyaan.pythonanywhere.com)

<img width="1911" height="990" alt="image" src="https://github.com/user-attachments/assets/5d8db19f-3b91-4699-a7cd-db94000889b1" />

<img width="1917" height="986" alt="image" src="https://github.com/user-attachments/assets/dc47b9a8-be50-48e2-8071-0779cc5d2c26" />

<img width="1919" height="987" alt="image" src="https://github.com/user-attachments/assets/4cfd0a3b-714d-4b24-bd80-bceccd33d9e9" />

<img width="1916" height="993" alt="image" src="https://github.com/user-attachments/assets/7682cc90-2b86-4985-9982-ca49397518e8" />


## What I Built

### Design & UI
- **Floating translucent navbar** — Infosys-style pill-shaped header with scroll effects, backdrop blur, and smooth transitions
- **Hero video section** — Full-screen looping background video with feature cards overlay
- **Dark cards on light theme** — High-contrast card design with cyan/purple accent colors
- **Hover zoom animations** — Smooth scale-up effects on 25+ interactive cards across all sections
- **Responsive design** — Fully mobile-optimized with bottom navigation bar, slide-out menu, and adaptive layouts

### Sections
- **Feature Grid** — 4 feature cards (Career Guidance, Study Materials, Interview Prep, Placement)
- **Top 5 Courses** — Dynamic course cards with images, fees, duration, and enquiry buttons
- **Excel with AT Academy** — Benefits grid with callback enquiry form
- **How It Works** — 4-step journey with animated icon circles and connector line
- **Career Services in a Nutshell** — 6 service cards with numbering
- **Testimonials** — Auto-scrolling marquee of student reviews
- **Success Stories** — Student achievement cards
- **CTA Banner** — Gradient call-to-action section

### Backend
- **18 Django models** — Courses, Branches, Testimonials, Blogs, Gallery, and more
- **Custom admin panel** — Branded admin site with full CRUD for all content
- **AJAX API endpoints** — Enquiry form, callback request, brochure download
- **Context processors** — Dynamic header/footer data from database
- **SQLite database** — Zero-configuration storage

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11+ | Core Programming |
| Django 6.x | Web Framework |
| SQLite | Database |
| HTML5 | Templates |
| Tailwind CSS | Styling (via CDN) |
| JavaScript | Interactive Elements, Animations |
| AJAX | Async Form Submissions |

---

## Project Structure

```
AT website/
├── .gitignore
├── atacademy/
│   ├── manage.py
│   ├── requirements.txt
│   ├── atacademy/              # Django project config
│   │   ├── settings.py         # Production-ready settings
│   │   ├── urls.py             # URL routing + media serving
│   │   └── wsgi.py
│   ├── core/                   # Main application
│   │   ├── models.py           # 18 database models
│   │   ├── admin.py            # Custom admin site
│   │   ├── views.py            # Views + API endpoints
│   │   ├── urls.py             # 26 URL patterns
│   │   ├── forms.py            # Enquiry/Callback forms
│   │   └── context_processors.py
│   ├── templates/              # 22 HTML templates
│   │   ├── base.html           # Base template with modals
│   │   ├── index.html          # Homepage (all sections)
│   │   ├── includes/
│   │   │   ├── header.html     # Floating navbar
│   │   │   └── footer.html
│   │   ├── course/             # Course list & detail
│   │   ├── branch/             # Branch detail
│   │   ├── blogs/              # Blog list & detail
│   │   ├── discover/           # About, Contact, Gallery, Videos
│   │   └── placements/         # Alumni & Recruiters
│   ├── static/
│   │   ├── images/             # Logo, favicon
│   │   └── videos/             # Hero video, experience video
│   └── media/                  # Uploaded content (gitignored)
```

---

## Setup (Local Development)

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/ayaan-2008/Full_Stack_website_.git
cd Full_Stack_website_/atacademy

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin account
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

Visit `http://localhost:8000`

---

## Production Deployment (PythonAnywhere)

The site is deployed on PythonAnywhere with the following setup:

1. Code pulled from GitHub
2. SQLite database uploaded separately
3. Static files served via Django's staticfiles
4. Media files served via Django's URL configuration
5. Auto-detection in `settings.py` sets `DEBUG=False` and configures `ALLOWED_HOSTS`

### Future Deployment Workflow
```bash
# Local: push changes
git add -A && git commit -m "description" && git push

# PythonAnywhere: pull and reload
cd ~/atacademy/atacademy
git pull
python3 manage.py migrate
# Click Reload on Web tab
```

---

## Admin Panel

**URL:** `https://AbdulAyaan.pythonanywhere.com/admin/`

### What's Editable
- **Site Settings** — Name, phone, email, address, social links, logos
- **Courses** — Name, category, fee, duration, image, description, brochure
- **Branches** — Name, address, phone, map URL
- **Testimonials** — Student name, course, feedback
- **Success Stories** — Student achievements
- **Hiring Partners** — Company name, logo
- **Certifications** — Certification names
- **Blogs** — Title, content, category
- **Gallery** — Images with categories

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/enquiry/` | Submit course enquiry |
| POST | `/api/callback/` | Request a callback |
| POST | `/api/brochure/<slug>/` | Download course brochure |
| POST | `/api/recruiter/` | Recruiter contact form |

---

## Database Models (18)

| Model | Description |
|-------|-------------|
| SiteSettings | Global site configuration |
| NavigationItem | Header menu items |
| FooterLinkGroup / FooterLink | Footer links |
| Course | Course listings |
| Branch | Branch locations |
| Programme | Course programmes |
| Technology | Tech stack display |
| Testimonial | Student testimonials |
| SuccessStory | Placement stories |
| HiringPartner | Partner companies |
| Certification | Available certifications |
| Blog | Blog posts |
| GalleryImage | Gallery photos |
| Enquiry / CallbackRequest | Form submissions |
| RecruiterContact / BrochureRequest | Inquiries |

---

## Security

- `SECRET_KEY` from environment variable (falls back to dev key locally)
- `DEBUG=False` on production
- CSRF protection on all forms
- Admin panel requires authentication
- `.gitignore` excludes `db.sqlite3`, `media/`, `.env`, `__pycache__/`

---

## License

MIT License

---

## Author

**Abdul Ayaan** — [GitHub](https://github.com/ayaan-2008)
