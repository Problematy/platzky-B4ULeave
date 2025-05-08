from flask import Flask, Response
from typing import Any, Dict

def process(app, plugin_config: Dict[str, Any]): # Defines the main `process` function taking a Flask app instance and plugin configuration
    # Store plugin configuration (defaults to empty dict)
    app.config['b4uleave'] = plugin_config or {}

    message = app.config['b4uleave'].get('message', 'Czy na pewno chcesz<br>opuścić naszą stronę?')

    @app.after_request # Decorator that registers a function to run after each request is processed
    def add_B4ULeave(response: Response) -> Response:
        if 'text/html' in response.headers.get('Content-Type', ''): # Function receives a Response object and returns a modified Response
            html = f"""
<style>
#B4ULeave-ModalWindow {{
  position: fixed;
  top: 0; left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}}
#B4ULeave-ModalWindow .B4ULeave-Content {{
  background: white;
  padding: 25px;
  border-radius: 10px;
  text-align: center;
  width: 400px;
  font-size: 20px;
  color: #245466;
  font-family: 'Poppins', sans-serif;
}}
#B4ULeave-ModalWindow .B4ULeave-Options {{
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 10px;
}}
#B4ULeave-ModalWindow .B4ULeave-Options button {{
  padding: 10px 15px;
  border: 2px solid #245466;
  background: white;
  color: #245466;
  font-size: 16px;
  cursor: pointer;
  border-radius: 5px;
}}
#B4ULeave-ModalWindow .B4ULeave-Options button:hover {{
  background: #245466;
  color: white;
}}
</style>

<div id="B4ULeave-ModalWindow">
  <div class="B4ULeave-Content">
    <p>{message}</p>
    <div class="B4ULeave-Options">
      <button id="B4ULeave-Stay">Zostań</button>
      <button id="B4ULeave-Leave">Wyjdź</button>
    </div>
  </div>
</div>

<script>
(function() {{
    var ModalWindow = document.getElementById('B4ULeave-ModalWindow');
    var Stay = document.getElementById('B4ULeave-Stay');
    var Leave = document.getElementById('B4ULeave-Leave');

    window.addEventListener('beforeunload', function(e) {{
        ModalWindow.style.display = 'flex';
        e.preventDefault();
        e.returnValue = '';
        return '';
    }});

    Stay.addEventListener('click', function() {{
        ModalWindow.style.display = 'none';
    }});

    Leave.addEventListener('click', function() {{
        ModalWindow.style.display = 'none';
        window.location.href = 'about:blank';
    }});
}})();
</script>"""
            response.set_data(response.get_data(as_text=True).replace('</body>', html + '</body>'))
        return response

    # temporary route for testing purposes
    # this route ensures that the plugin can modify a simple HTML response
    def index():
        return "<html><body>Hello</body></html>"
    app.route("/")(index)

    return app