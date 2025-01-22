from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-scripts', methods=['POST'])
def run_scripts():
    try:
        # Execute scripts securely
        result_check_trigger = subprocess.run(
            ['python3', 'check_and_trigger.py'], 
            check=True, 
            capture_output=True, 
            text=True
        )
        
        result_maha = subprocess.run(
            ['python3', 'maha.py'], 
            check=True, 
            capture_output=True, 
            text=True
        )
        
        # Combine results to return to the user
        combined_output = (
            f"Check and Trigger Output:\n{result_check_trigger.stdout}\n\n"
            f"Maha Output:\n{result_maha.stdout}"
        )
        
        return render_template(
            'index.html', 
            message="Scripts executed successfully!", 
            details=combined_output
        )

    except subprocess.CalledProcessError as e:
        # Handle script errors
        error_message = f"Error occurred while running scripts: {e.stderr or str(e)}"
        return render_template('index.html', message=error_message)

    except Exception as e:
        # Handle other errors
        return render_template('index.html', message=f"Unexpected error: {str(e)}")

if __name__ == '__main__':
    # Use debug mode only during development
    app.run(debug=True)