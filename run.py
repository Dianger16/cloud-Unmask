import os
from app.ui import app


if __name__ == "__main__":
    
    print(f"[DEBUG] Current working directory: {os.getcwd()}")
    print(f"[DEBUG] Template directory expected at: {os.path.join(os.getcwd(), 'templates')}")

    
    app.run(debug=True)
