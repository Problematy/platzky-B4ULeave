from flask import Flask, Response
from typing import Any, Dict

def process(app, plugin_config: Dict[str, Any]): # Defines the main `process` function taking a Flask app instance and plugin configuration
    # Store plugin configuration (defaults to empty dict)
    app.config['b4uleave'] = plugin_config or {}

    message = app.config['b4uleave'].get('message', 'Czy na pewno chcesz<br>opuścić naszą stronę?')
    stay = app.config['b4uleave'].get('stay', 'Stay')
    leave = app.config['b4uleave'].get('leave', 'Leave')

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

<div id="B4ULeave-ModalWindow" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; 
     background:rgba(0,0,0,0.5); align-items:center; justify-content:center; z-index:9999;">
  <div class="B4ULeave-Content" style="background:white; padding:2rem; border-radius:8px; max-width:90%; text-align:center;">
    <p>{message}</p>
    <div class="B4ULeave-Options" style="margin-top:1rem;">
      <button id="B4ULeave-Stay">{stay}</button>
      <button id="B4ULeave-Leave">{leave}</button>
    </div>
  </div>
</div>

<script>
(function() {{

    var ModalWindow = document.getElementById('B4ULeave-ModalWindow');
    var Stay        = document.getElementById('B4ULeave-Stay');
    var Leave       = document.getElementById('B4ULeave-Leave');

    // get the confirmation message from the <p> element
    var confirmationMessage = ModalWindow.querySelector('p').innerText;

    // flag to prevent multiple displays
    var hasShown = false;

    // detect first cursor exit from the page
    document.addEventListener('mouseout', function(e) {{
        e = e || window.event;
        var from = e.relatedTarget || e.toElement;
        // no relatedTarget means the cursor left the document area
        if (!from && e.clientY <= 0 && !hasShown) {{
            hasShown = true;
            ModalWindow.style.display = 'flex';
        }}
    }});

    // hide modal when user chooses to stay
    Stay.addEventListener('click', function() {{
        ModalWindow.style.display = 'none';
    }});

    // hide modal and redirect when user chooses to leave
    Leave.addEventListener('click', function() {{
        ModalWindow.style.display = 'none';
        window.location.href = 'about:blank';
    }});
}})();
</script>"""
            response.set_data(response.get_data(as_text=True).replace('</body>', html + '</body>'))
        return response

    return app