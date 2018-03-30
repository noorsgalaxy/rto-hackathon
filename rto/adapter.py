from allauth.account.adapter import DefaultAccountAdapter

class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        user = request.user
        try:
            group = user.groups.all().first().name
        except:
            group = None
        print user,group,type(group)
        if group == "rto":
            url = "/admin"
        elif group == "police":
            url = "/mud/policedash"
        elif group == "pollution_control":
            url = "/"
        else:
            url = "/mud/userdash"
        print url
        return url
