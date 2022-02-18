from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    verbose_name = '博客'
# 默认为article, 此处需要手动修改为blog.article, 以解决如下报错Cannot import 'demo'. Check that 'apps.demo.apps.DemoConfig.name' is correc