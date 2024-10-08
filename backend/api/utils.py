

def get_ip(request):
    data = request.META.get('HTTP_X_FORWARDED_FOR')
    if data:
        return data.split(',')[0]
    return request.META.get('REMOTE_ADDR')
    