from django.conf import settings
from django.views.generic import TemplateView
from github import Github

from code_risk_auditor.models import InstalledApps
from main import git_integration


class HomeView(TemplateView):
    template_name = "code_risk_auditor/home.html"

class InstalledAppCallbackView(TemplateView):
    template_name = "code_risk_auditor/installed_app_callback.html"

    def get(self, request, *args, **kwargs):
        installation_id = request.GET.get('installation_id')
        code = request.GET.get('code')
        setup_action = request.GET.get('setup_action')

        print(f"installation_id: {installation_id}")
        print(f"code: {code}")
        print(f"setup_action: {setup_action}")

        # We want an access_token for the given user
        if setup_action == 'install':
            # We ensure that the installation matches the logged in user
            git_connection = Github(
                login_or_token=git_integration.get_access_token(
                    installation_id
                ).token
            )

            g = Github()

            app = g.get_oauth_application(settings.GITHUB_CLIENT_ID, settings.GITHUB_CLIENT_SECRET)

            token = app.get_access_token(code)

            print("My Token is...", token)

            mygh = Github(login_or_token=token.token).get_user()

            print("User has repos")
            for repo in mygh.get_repos():
                print(repo.name)

            # Check if the installation is for this user
            is_valid = False

            for installation in mygh.get_installations():
                if installation.id == int(installation_id):
                    is_valid = True
                    break

            print("Installation is VALID: ", is_valid)


            if is_valid:
                if not InstalledApps.objects.filter(installation_id=installation_id).exists():

                    InstalledApps.objects.create(
                        owner=request.user,
                        installation_id=installation_id,
                        code=code
                    )
                else:
                    print("Duplicate callback call!")
            else:
                print("Invalid request (WTF?)")

        return super().get(request, *args, **kwargs)


