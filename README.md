# Django + ChatterBot Terminal Chat Client

A terminal client that lets you chat with a bot built with **Django** and
**ChatterBot**. ChatterBot is a machine-learning based conversational dialog
engine that generates responses from collections of known conversations.
Everything the bot learns is stored in Django's database through ChatterBot's
`DjangoStorageAdapter`.

```
user: Good morning! How are you doing?
bot: I am doing very well, thank you for asking.
user: You're welcome.
bot: Do you like hats?
```

![Terminal chat session](screenshots/03_chat_session.png)

## Project structure

```
django-chatterbot-terminal/
├── manage.py                     # Django command-line entry point
├── requirements.txt              # Manifest of Python dependencies
├── MANIFEST.in                   # Packaging manifest (files to include)
├── chatbot_project/
│   ├── settings.py               # Django + ChatterBot configuration
│   ├── urls.py                   # Admin URL (browse trained statements)
│   ├── wsgi.py / asgi.py
└── chat/                         # The chat app
    ├── bot.py                    # get_chatbot(): builds the ChatBot from settings
    ├── training_data.py          # Custom training conversations
    ├── tests.py                  # Unit tests
    └── management/commands/
        ├── train_bot.py          # python manage.py train_bot
        └── chat.py               # python manage.py chat  (terminal client)
```

## Setup

Requires Python 3.9–3.12 (tested on 3.11).

```bash
# 1. Clone and enter the project
git clone <your-repo-url>
cd django-chatterbot-terminal

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 3. Install dependencies (includes the spaCy English model)
pip install -r requirements.txt

# 4. Create the database tables (including ChatterBot's Statement/Tag tables)
python manage.py migrate

# 5. Train the bot (English corpus + custom conversations, ~20 s)
python manage.py train_bot
```

## Usage

```bash
python manage.py chat
```

Type a message after `user:` and press Enter. Type `quit`, `exit` or `bye`
(or press Ctrl+C) to end the session.

Options:

| Command | Purpose |
| --- | --- |
| `python manage.py chat --read-only` | Chat without the bot learning from the conversation |
| `python manage.py train_bot --no-corpus` | Train only on `chat/training_data.py` (fast) |
| `python manage.py train_bot --reset` | Clear everything the bot has learned, then retrain |
| `python manage.py test` | Run the unit tests |

## How it works

1. `settings.py` adds `chatterbot.ext.django_chatterbot` to `INSTALLED_APPS`
   and sets the `CHATTERBOT` dictionary (storage adapter + `BestMatch` logic
   adapter).
2. `train_bot` uses `ChatterBotCorpusTrainer` (English corpus) and
   `ListTrainer` (custom conversations) to store statement/response pairs in
   the database.
3. `chat` reads a line with `input()`, calls `chatbot.get_response()` and
   prints the reply, looping until the user exits.

## References

- ChatterBot documentation: https://chatterbot.readthedocs.io/en/stable/
- ChatterBot Django integration: https://chatterbot.readthedocs.io/en/stable/django/index.html
- Django: https://www.djangoproject.com/
