# Flashcards — Study Made Simple

A minimalist, open-source flashcard web app to help you study smarter, not harder. Create custom flashcards and practice them interactively — for free, with no signups or clutter.

---

##  Features

-  Add custom flashcards (keyword + definition)
- Practice mode with random flashcards
-  Reveal answers by clicking cards
-  Friendly error handling and validations
-  Clean, responsive Bootstrap design

---

##  Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap 5, JavaScript
- **Database**: SQLite (default Django DB)

---

## Pages

| Page           | Functionality                          |
|----------------|-----------------------------------------|
| Welcome Page   | Entry point with navigation             |
| Add Flashcard  | Form to create a flashcard              |
| Practice Page  | Click-to-flip flashcards, one at a time |

---

## Setup Instructions

```bash
# Clone the repo
git clone https://github.com/your-username/flashcards.git
cd flashcards

# Create virtual environment
python -m venv venv
source venv/bin/activate  # on Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
