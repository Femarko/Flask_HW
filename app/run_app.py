from app import adv
from app.web import urls
from app.data.db import init_db

if __name__ == "__main__":
    adv.run(debug=True)
