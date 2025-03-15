# GitHub Activity Bot

A simple GitHub Actions bot that creates 5 random commits every day to maintain repository activity.

## How it works

This bot uses GitHub Actions to run a Python script daily at midnight UTC. The script:
1. Creates or updates a file called `random_changes.txt`
2. Makes 5 commits with random content
3. Each commit includes a timestamp and random string

## Setup

1. Push this code to your GitHub repository
2. The GitHub Actions workflow will automatically run daily
3. You can also manually trigger the workflow from the Actions tab

## Files

- `.github/workflows/daily-commits.yml`: GitHub Actions workflow configuration
- `commit_script.py`: Python script that creates the commits
- `requirements.txt`: Dependencies (none required)
- `random_changes.txt`: File that gets modified with random content

## Note

This bot is for demonstration purposes only. Please use responsibly and in accordance with GitHub's terms of service. 