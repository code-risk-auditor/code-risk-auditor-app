# Test
from github import GithubIntegration, Github

app_id ="Iv23li2Pwc8kbCDC3by3"
with open(
        "code-risk-auditor.2024-06-04.private-key.pem",
        'r'
) as cert_file:
    app_key = cert_file.read()

git_integration = GithubIntegration(
    app_id,
    app_key,
)

# print("Hello")
#
# # Get all installations?!
# for installation in git_integration.get_installations():
#     print(installation.id)
#
#     for repo in installation.get_repos():
#         print("Repo: ", repo.name)
# #
# git_connection = Github(
#         login_or_token=git_integration.get_access_token(
#             git_integration.get_installations()[0].id
#         ).token
#     )

# print("Token: ", git_connection.get_repos())