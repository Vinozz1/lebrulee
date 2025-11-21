# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "flask>=3.0.0",
#     "flask-sqlalchemy>=3.1.1",
#     "flask-login>=0.6.3",
#     "flask-bcrypt>=1.0.1",
# ]
# ///

from app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="127.0.0.1", port=5000)