from django.contrib.auth.models import User
user = User.objects.create_user('test', 'test@thebeatles.com', 'test')
