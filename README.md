# AT Academy - Full Stack Website

A fully-featured Django backend for **AT Academy** (formerly Teks Academy) — an educational institution website with a complete admin panel, dynamic content management, and responsive templates matching the original site design.

---

## Features

- **Django 6.0.6 Backend** — Clean, scalable Python web framework
- **SQLite Database** — Lightweight, zero-configuration storage
- **Custom Admin Panel** — Branded `ATAdminSite` with full CRUD for all content
- **18 Database Models** — Courses, Branches, Testimonials, Blogs, Gallery, and more
- **Dynamic Content** — Every piece of text, image, and link editable from admin
- **Responsive Templates** — Mobile-first design matching the original AT Academy site
- **API Endpoints** — Enquiry form, Callback request, Recruiter contact (AJAX-powered)
- **Context Processors** — Dynamic header/footer data from database
- **Image Uploads** — Admin-uploadable logos, banners, and feature icons

---

## Project Structure

```
AT website/
├── .gitignore
├── Start Website.bat              # One-click launcher
├── atacademy/
│   ├── manage.py
│   ├── atacademy/                 # Django project settings
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── core/                      # Main application
│   │   ├── models.py              # 18 database models
│   │   ├── admin.py               # Custom admin site
│   │   ├── views.py               # 20 views + 3 API endpoints
│   │   ├── urls.py                # URL routing
│   │   ├── forms.py               # Enquiry/Callback/Recruiter forms
│   │   ├── context_processors.py  # Global template context
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── import_data.py # Data import command
│   │   └── migrations/            # Database migrations (0001-0004)
│   ├── templates/                 # 22 HTML templates
│   │   ├── base.html              # Base template with modals
│   │   ├── index.html             # Homepage
│   │   ├── includes/
│   │   │   ├── header.html        # Dynamic header with dropdowns
│   │   │   └── footer.html        # Dynamic footer from settings
│   │   ├── course/                # Course list & detail
│   │   ├── branch/                # Branch detail
│   │   ├── blogs/                 # Blog list & detail
│   │   ├── discover/              # About, Contact, Gallery, Videos
│   │   └── placements/            # Alumni & Recruiters
│   ├── static/
│   │   └── images/
│   │       └── at_academy_logo.png
│   └── db.sqlite3                 # SQLite database (gitignored)
```

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.14 | Core Programming |
| Django 6.0.6 | Web Framework |
| SQLite | Database |
| HTML5 | Templates |
| Tailwind CSS (CDN) | Styling |
| JavaScript | Interactive Elements |
| AJAX | Form Submissions |

---

## Setup

### Prerequisites

- Python 3.14+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/ayaan-2008/Full_Stack_website_.git
cd Full_Stack_website_
```

### 2. Install dependencies

```bash
cd atacademy
pip install django django-cleanup
```

### 3. Run migrations

```bash
python manage.py migrate
```

### 4. Create admin account

```bash
python manage.py createsuperuser
```

### 5. Import initial data (optional)

```bash
python manage.py import_data
```

### 6. Start the server

```bash
python manage.py runserver 0.0.0.0:8000
```

Or double-click **`Start Website.bat`** to launch everything automatically.

---

## Access

| Page | URL |
|------|-----|
| Website | http://localhost:8000 |
| Admin Panel | http://localhost:8000/admin/ |

### Default Admin Credentials

| Field | Value |
|-------|-------|
| Username | admin |
| Password | admin123 |

---

## Admin Panel — What's Editable

### Site Settings
- Site name & tagline
- Phone number, email, address
- Google Maps URL
- Social media links
- Header & footer logos

### Home Page Settings
- Career Guidance icon
- Study Materials icon
- Interview Prep icon
- Placement Assistance icon
- Excel banner image

### Nutshell / Career Services
- Section illustration
- 6 feature icons (Seminars, Resume, Mock Interviews, Placement, Internship, Projects)

### Content Management
- **Courses** — Name, category, fee, duration, slug, image, description
- **Branches** — Name, address, phone, slug, map URL
- **Testimonials** — Student name, course, feedback
- **Success Stories** — Student achievements
- **Hiring Partners** — Company name, logo
- **Certifications** — Certification names
- **Blogs** — Title, content, category, date
- **Gallery** — Images with categories
- **Navigation** — Menu items with dropdowns
- **Footer** — Link groups and links

---

## Database Models

| Model | Description |
|-------|-------------|
| SiteSettings | Global site configuration (singleton) |
| NavigationItem | Header menu items |
| FooterLinkGroup | Footer link categories |
| FooterLink | Individual footer links |
| SearchedTerm | Search suggestions |
| Technology | Tech stack display |
| Course | Course listings |
| Branch | Branch locations |
| Programme | Course programmes |
| Testimonial | Student testimonials |
| SuccessStory | Placement success stories |
| HiringPartner | Partner companies |
| Certification | Available certifications |
| Blog | Blog posts |
| GalleryImage | Gallery photos |
| Enquiry | Form submissions |
| CallbackRequest | Callback requests |
| RecruiterContact | Recruiter inquiries |

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/enquiry/` | Submit course enquiry |
| POST | `/api/callback/` | Request a callback |
| POST | `/api/recruiter/` | Recruiter contact form |

All endpoints accept JSON and return JSON responses.

---

## Key Routes

| Route | Page |
|-------|------|
| `/` | Homepage |
| `/course/` | All Courses |
| `/courses/<slug>/` | Course Detail |
| `/branch/<slug>/` | Branch Detail |
| `/discover/about-us/` | About Us |
| `/discover/contact-us/` | Contact Us |
| `/discover/gallery/` | Photo Gallery |
| `/discover/videos/` | Videos |
| `/blogs/` | Blog List |
| `/placements/alumni/` | Alumni Stories |
| `/placements/recruiters/` | Recruiters |
| `/success-stories/` | Success Stories |
| `/privacy-policy/` | Privacy Policy |
| `/policyagreements/terms-of-service/` | Terms of Service |
| `/apply-for-jobs/` | Job Application |
| `/find-my-course/` | Course Finder |

---

## Security Notes

- `SECRET_KEY` is read from the `DJANGO_SECRET_KEY` environment variable
- Falls back to a dev key for local development
- Admin panel requires authentication
- CSRF protection enabled on all forms
- `db.sqlite3` and `media/` are gitignored

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## Author

Developed by **Abdul Ayaan**
