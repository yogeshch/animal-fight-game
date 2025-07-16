# Animal Fighter Web App

A modern web version of the Animal Fighter game, where you battle the computer using real animal images!

## Features
- Clean, modern, light-themed UI (Bootstrap)
- Select 3 animals for battle from 10 real animal images
- Step-by-step battle rounds with images and powers
- Animated, responsive interface
- Final results and round-by-round summary
- Play again or exit at any time

## Setup & Requirements
- Python 3.x
- Flask (`pip install flask`)
- All animal images (`lion.jpg`, `tiger.jpg`, etc.) in `static/images/` (150x150 recommended)

## How to Run Locally
1. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Mac/Linux
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   python app.py
   ```
4. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Deployment
- For production, use a WSGI server (e.g., Gunicorn, uWSGI) and set `debug=False` in `app.py`.
- You can deploy to platforms like Heroku, PythonAnywhere, or your own server.

## Folder Structure
- `app.py` - Main Flask app
- `game_logic.py` - Game logic (no UI dependencies)
- `templates/` - HTML templates (Jinja2)
- `static/images/` - Animal images
- `static/css/` - Custom CSS

## Credits
- Animal images: Your own or royalty-free sources
- UI: Bootstrap 5

Enjoy your Animal Fighter web game! 