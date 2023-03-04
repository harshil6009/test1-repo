from github import Github

# Replace 'your-access-token' with your personal access token
g = Github('your-access-token')

# Replace 'your-username' with your GitHub username
user = g.get_user('your-username')

# Replace 'test-repo' with the name of your repository
repo = user.get_repo('test-repo')

# Do something with the repository, such as getting its name and description
print(f"Repository name: {repo.name}")
print(f"Repository description: {repo.description}")
