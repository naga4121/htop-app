from flask import Flask
import subprocess
import datetime
import os

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "sample_name"
    user = os.getenv("USER", "codespace")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    # Run 'top -b -n 1' to get top output
    try:
        top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    except Exception as e:
        top_output = f"Error retrieving top output: {e}"

    # Format the response in <pre> for preserving formatting
    return f"""
    <pre>
Name: {name}
User: {user}
Server Time (IST): {now}
TOP output:
{top_output}
    </pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
