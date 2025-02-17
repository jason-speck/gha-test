import webview
from importlib.metadata import version

try:
    __version__ = version("hello")
except ImportError:
    __version__ = "0.1"  # Fallback for development

__version_info__ = (0, 1)  # (major, minor)

class Api:
    def get_message(self):
        """Simple API method that returns a greeting message"""
        return "Hello from Python backend!"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello World V0.2 bump</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f2f5;
        }
        .container {
            text-align: center;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        button {
            padding: 10px 20px;
            margin-top: 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello World!</h1>
        <p id="message">Welcome to PyWebView</p>
        <button onclick="getMessage()">Get Message from Python</button>
    </div>

    <script>
        async function getMessage() {
            try {
                const message = await window.pywebview.api.get_message();
                document.getElementById('message').textContent = message;
            } catch (error) {
                console.error('Error:', error);
            }
        }
    </script>
</body>
</html>
"""

def main():
    # Create API instance
    api = Api()
    
    # Create window with HTML content directly
    window = webview.create_window(
        title='PyWebView Hello World',
        html=HTML,  # Use html parameter instead of url
        js_api=api,
        width=800,
        height=600
    )
    
    # Start the application
    webview.start(debug=True)

if __name__ == '__main__':
    main()
