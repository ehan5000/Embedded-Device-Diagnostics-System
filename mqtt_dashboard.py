import random
import time
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# Simulated device data (would normally come from serial or MQTT)
device_state = {"temp": 0, "voltage": 0, "status": "OK"}

@app.route('/')
def dashboard():
    html = """
    <html>
    <head>
        <title>Embedded Device Diagnostics</title>
        <meta http-equiv="refresh" content="1">
        <style>
            body { font-family: Arial; text-align: center; background-color: #f5f5f5; }
            .box { background-color: white; padding: 20px; margin: 40px auto; width: 300px;
                   border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.2); }
            h1 { color: #333; }
            .ok { color: green; font-weight: bold; }
            .fault { color: red; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>Device Diagnostics</h1>
            <p>Temperature: {{temp}}°C</p>
            <p>Voltage: {{voltage}} mV</p>
            <p>Status: <span class="{{status_class}}">{{status}}</span></p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, 
                                  temp=device_state["temp"], 
                                  voltage=device_state["voltage"],
                                  status=device_state["status"],
                                  status_class="ok" if device_state["status"] == "OK" else "fault")

def simulate_data():
    """Generate telemetry data."""
    while True:
        device_state["temp"] = random.randint(25, 85)
        device_state["voltage"] = random.randint(3000, 3500)
        device_state["status"] = "FAULT" if random.random() < 0.1 else "OK"
        time.sleep(1)

if __name__ == '__main__':
    import threading
    threading.Thread(target=simulate_data, daemon=True).start()
    app.run(debug=False, port=5000)
