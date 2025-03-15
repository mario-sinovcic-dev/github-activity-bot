import os
import random
import string
from datetime import datetime
import subprocess

def generate_random_string(length=10):
    """Generate a random string of specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_random_change():
    """Create a random change in a file."""
    # Create or update a file with random content
    with open('random_changes.txt', 'a') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        random_content = generate_random_string()
        f.write(f"{timestamp}: {random_content}\n")

def make_commit(message):
    """Make a commit with the given message."""
    subprocess.run(['git', 'add', 'random_changes.txt'])
    subprocess.run(['git', 'commit', '-m', message])
    subprocess.run(['git', 'push'])

def main():
    # Configure git with GitHub email and name from environment variables
    git_email = os.environ.get('GIT_EMAIL')
    git_name = os.environ.get('GIT_NAME')
    
    if not git_email or not git_name:
        raise ValueError("GIT_EMAIL and GIT_NAME environment variables must be set")
    
    subprocess.run(['git', 'config', '--global', 'user.email', git_email])
    subprocess.run(['git', 'config', '--global', 'user.name', git_name])
    
    # Create 5 commits
    for i in range(5):
        create_random_change()
        commit_message = f"Daily commit #{i+1}: {generate_random_string(5)}"
        make_commit(commit_message)

if __name__ == "__main__":
    main() 