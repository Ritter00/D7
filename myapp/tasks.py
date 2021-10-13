from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Post, Category, PostCategory
from datetime import datetime, timedelta


@shared_task
def send_mail(pk):
    post = Post.objects.get(id=pk)
    category = post.postCategory.all().last()
    mail = []
    for subscriber in category.subscribers.all():
        mail.append(subscriber.email)
    html_content = render_to_string('new_post.html',
                                                {'new_post': post,
                                                 'cat': category
                                                 },
                                                )  # получаем наш html
    msg = EmailMultiAlternatives(
                    subject=f'Новый пост в разделе {category}',
                    body=instance.title,
                    from_email='oOo.example@yandex.ru',
                    to=mail,
                )
    msg.attach_alternative(html_content, 'text/html')  # добавляем html
    msg.send()


@shared_task
def spam():
    catgories = Category.objects.all()
    time = datetime.now() - timedelta(days=7)

    for category in catgories:
        posts = Post.objects.filter(postCategory=category.id).filter(dateCreation__date__gte=time)
        subs = category.subscribers.all()
        mail = []
        cat = category

        for sub in subs:
            mail.append(sub.email)
        html_content = render_to_string('spam.html',
                                        {'posts': posts,
                                         'cat': cat,
                                         },
                                        )  # получаем наш html
        msg = EmailMultiAlternatives(
            subject=f'Новые посты в разделе {cat}',
            body='Привет',
            from_email='oOo.example@yandex.ru',
            to=mail,
        )
        msg.attach_alternative(html_content, 'text/html')  # добавляем html
        msg.send()
