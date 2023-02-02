from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('about/', views.about, name='about'),
    path('hello/', views.home, name='hello'),
    path('hello/<str:username>', views.hello),
    path('hello/<int:id>', views.hello_id),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('projects/new', views.create_project, name="new_project"),
    path('projects/update/<int:id>', views.update_project, name='update_project'),
    path('projects/delete/<int:id>', views.remove_project, name='remove_project'),
    path('tasks/', views.tasks, name="tasks"),
    path('tasks/<int:id>', views.get_task_by_id, name="task_by_id"),
    path('tasks/new', views.create_task, name="new_task"),
]
