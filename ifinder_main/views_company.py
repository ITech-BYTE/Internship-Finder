from ifinder_main.views import register

# COMPANY REGISTRATION
def register_company(request):
    return register(request, 1)