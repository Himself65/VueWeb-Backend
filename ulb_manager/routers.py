from rest_framework import routers
from blog.views import ArticleViewSet
from user.views import UserRegisterViewSet
# from user.views import

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)  #文章API
router.register(r'register', UserRegisterViewSet)  #注册API
