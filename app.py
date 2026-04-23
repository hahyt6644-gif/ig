import os, threading
from flask import Flask
import your_tool_file  # Import your scanner script

app = Flask(__name__)

@app.route('/')
def status():
    return "Bot is Active"

if __name__ == "__main__":
    # Start your tool logic in the background
    # Ensure your tool's main loop is inside a function
    threading.Thread(target=your_tool_file.x7s1evipfree, daemon=True).start()
    
    # Start Flask
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  
