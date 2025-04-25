from flask import Flask, Response
from typing import Any, Dict

def process(app, plugin_config: Dict[str, Any]): 
    # Defines the main `process` function taking a Flask app instance and plugin configuration
    # Store plugin configuration (defaults to empty dict)
    app.config['B4ULeave'] = plugin_config or {}

    @app.after_request
    def add_B4ULeave(response: Response) -> Response:
      # Decorator that registers a function to run after each request is processed
        if 'text/html' in response.headers.get('Content-Type', ''):
          # Function receives a Response object and returns a modified Response
            html = f"""
<style>
#B4ULeave-OknoModalne {{
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
#B4ULeave-OknoModalne .B4ULeave-Zawartosc {{
  background: white;
  padding: 25px;
  border-radius: 10px;
  text-align: center;
  width: 400px;
  font-size: 20px;
  color: #245466;
  font-family: 'Poppins', sans-serif;
}}
#B4ULeave-OknoModalne .B4ULeave-Opcje {{
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 10px;
}}
#B4ULeave-OknoModalne .B4ULeave-Opcje button {{
  padding: 10px 15px;
  border: 2px solid #245466;
  background: white;
  color: #245466;
  font-size: 16px;
  cursor: pointer;
  border-radius: 5px;
}}
#B4ULeave-OknoModalne .B4ULeave-Opcje button:hover {{
  background: #245466;
  color: white;
}}
</style>

<div id="B4ULeave-OknoModalne">
  <div class="B4ULeave-Zawartosc">
    <p>Czy na pewno chcesz<br>opuścić naszą stronę?</p>
    <div class="B4ULeave-Opcje">
      <button id="B4ULeave-Zostan">Zostań</button>
      <button id="B4ULeave-Wyjdz">Wyjdź</button>
    </div>
  </div>
</div>

<script>
(function() {{
    var OknoModalne = document.getElementById('B4ULeave-OknoModalne');
    var Zostan = document.getElementById('B4ULeave-Zostan');
    var Wyjdz = document.getElementById('B4ULeave-Wyjdz');

    window.addEventListener('beforeunload', function(e) {{
        OknoModalne.style.display = 'flex';
        e.preventDefault();
        e.returnValue = '';
        return '';
    }});

    Zostan.addEventListener('click', function() {{
        OknoModalne.style.display = 'none';
    }});

    Wyjdz.addEventListener('click', function() {{
        OknoModalne.style.display = 'none';
        window.location.href = 'about:blank';
    }});
}})();
</script>"""
            response.set_data(response.get_data(as_text=True).replace('</body>', html + '</body>'))
        return response

    return app