import requests
import time

def check_for_new_commits(owner, repo, last_known_commit=None):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    
    if response.status_code == 200:
        commits = response.json()
        latest_commit_sha = commits[0]['sha']
        print(commits)
        if last_known_commit != latest_commit_sha:
            print(f"Новый коммит обнаружен: {latest_commit_sha}")
            return latest_commit_sha
        else:
            print("Новых коммитов нет")
            return last_known_commit
    else:
        print(f"Ошибка при запросе: {response.status_code}")
        return last_known_commit

# Пример использования
owner = "Shrekami"
repo = "Tkinter_tutorials"
last_commit = None

while True:
    last_commit = check_for_new_commits(owner, repo, last_commit)
    time.sleep(300)  # Проверка каждые 5 минут