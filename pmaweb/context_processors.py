from files.models import Release


def releases(request):
    latest = Release.objects.filter(stable=True)[0]
    beta = Release.objects.filter(stable=False)[0]
    if beta.version_num < latest.version_num:
        beta = None
    return {
        'latest': latest,
        'beta': beta,
    }
