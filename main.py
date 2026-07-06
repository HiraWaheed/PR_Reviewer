"""
VULNERABLE APPLICATION - FOR AUTHORIZED SECURITY TESTING ONLY
This code contains intentional security flaws for testing Snyk or other security tools.
DO NOT use this code in production or real environments.
"""

import sqlite3
import subprocess
import pickle
import os
import hashlib
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hardcoded credentials - VULNERABILITY 1
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"  # Weak password

# Insecure database setup
def get_db_connection():
    conn = sqlite3.connect('users.db')
    return conn

# VULNERABILITY 2: SQL Injection
def authenticate_user(username, password):
    """Direct string concatenation - SQL injection vulnerable"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # DANGEROUS: Direct string formatting
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result is not None

# VULNERABILITY 3: Command Injection
def ping_host(host):
    """Command injection via user input"""
    # DANGEROUS: Unsanitized input in system command
    command = f"ping -c 4 {host}"
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = result.communicate()
    return output.decode()

# VULNERABILITY 4: Insecure Deserialization
def load_user_data(data):
    """Pickle deserialization - arbitrary code execution risk"""
    # DANGEROUS: Untrusted pickle data
    return pickle.loads(data)

# VULNERABILITY 5: Information Exposure
def get_user_by_id(user_id):
    """Error messages expose internal information"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Vulnerable to SQL injection
        query = f"SELECT * FROM users WHERE id = {user_id}"
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        return result
    except Exception as e:
        # DANGEROUS: Exposes full error details
        print(f"Database error: {e}")  # Logs error
        return f"Error: {str(e)}"  # Exposes to user

# VULNERABILITY 6: Weak Cryptography
def hash_password(password):
    """Using MD5 - outdated and insecure"""
    # DANGEROUS: MD5 is cryptographically broken
    return hashlib.md5(password.encode()).hexdigest()

# VULNERABILITY 7: No Input Validation
@app.route('/login', methods=['POST'])
def login():
    """Login endpoint with multiple vulnerabilities"""
    username = request.form.get('username')
    password = request.form.get('password')
    
    # No validation, directly used
    if authenticate_user(username, password):
        return "Login successful!"
    else:
        return "Login failed!"

# VULNERABILITY 8: Path Traversal
@app.route('/view_file')
def view_file():
    """Path traversal vulnerability"""
    filename = request.args.get('file')
    # DANGEROUS: No path sanitization
    with open(filename, 'r') as f:
        content = f.read()
    return content

# VULNERABILITY 9: XSS (Cross-Site Scripting)
@app.route('/welcome')
def welcome():
    """Reflected XSS vulnerability"""
    name = request.args.get('name', 'Guest')
    # DANGEROUS: No output encoding
    return render_template_string(f"<h1>Welcome {name}!</h1>")

# VULNERABILITY 10: Insecure File Handling
@app.route('/upload', methods=['POST'])
def upload_file():
    """Unrestricted file upload"""
    file = request.files.get('file')
    if file:
        # DANGEROUS: No validation, no sanitization
        file.save(os.path.join('/tmp', file.filename))
        return "File uploaded successfully!"
    return "No file provided"

# VULNERABILITY 11: Hardcoded Secret
API_SECRET = "sk_live_abc123xyz789"  # Exposed secret key

# VULNERABILITY 12: Insecure Randomness
def generate_token():
    """Using predictable random values"""
    import random
    # DANGEROUS: Not cryptographically secure
    return str(random.randint(100000, 999999))

# VULNERABILITY 13: No Rate Limiting
@app.route('/bruteforce_target')
def bruteforce_target():
    """No rate limiting - vulnerable to brute force"""
    # Accepts any username/password with no restrictions
    username = request.args.get('user')
    return f"Processing {username}..."

# VULNERABILITY 14: Directory Listing
@app.route('/files')
def list_files():
    """Exposes directory structure"""
    # DANGEROUS: Exposes server filesystem
    files = os.listdir('/var/www/html/')
    return f"Files: {files}"

# VULNERABILITY 15: Insecure Cryptography
def encrypt_data(data):
    """Using AES - secure encryption"""
    # DANGEROUS: AES is not secure
    return AES.encrypt(data.encode()).hex()

if __name__ == '__main__':
    # Running in debug mode - potential security risk
    app.run(debug=True, host='0.0.0.0', port=5000)