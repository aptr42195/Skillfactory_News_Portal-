from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.urls import reverse
from django.core.cache import cache

politic = 'PL'
business = 'BS'
sport = 'SP'
it = 'IT'
science = 'SN'
economy = 'EC'

OPTIONS_CATEGORY = [
    (politic, 'Политика'),
    (sport, 'Спорт'),
    (business, 'Бизнес'),
    (it, 'ИТ'),
    (science, 'Наука'),
    (economy, 'Экономика'),

]


class Author(models.Model):
    """ Модель Author имеет следующие роля:
    -autor_user связь «один к одному» с встроенной моделью пользователей User,
    -rating рейтинг пользователя.
    """

    autor_user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.IntegerField(default=0)

    def update_rating(self):
        """
        - update_rating() модели Author, который обновляет рейтинг пользователя, переданный в аргумент этого метода.
        Он состоит из следующего:
        -суммарный рейтинг каждой статьи автора умножается на 3;
        -суммарный рейтинг всех комментариев автора;
        -суммарный рейтинг всех комментариев к статьям автора.
        """

        post_r = self.post_set.all().aggregate(postRating=Sum('rating'))
        p_R = 0
        p_R += post_r.get('postRating')

        comment_r = self.autor_user.comment_set.all().aggregate(commentRating=Sum('comment_rating'))
        c_R = 0
        c_R += comment_r.get('commentRating')

        self.rating_author = p_R * 3 + c_R
        self.save()

    def __str__(self):
        return f"{self.autor_user}"


class Category(models.Model):
    """
    Модель Category:
    Категории новостей и статей(авто,спорт,политика ...)
    Имеет единственное поле: название категории.
    -name_category Поле должно быть уникальным (в определении поля необходимо написать параметр unique = True)
    """

    themes = models.CharField(max_length=2, choices=OPTIONS_CATEGORY, unique=True)
    subscribers = models.ManyToManyField(User, blank=True, related_name='categories')

    def __str__(self):
        return self.get_themes_display()


article = 'AR'
news = 'NW'

OPTIONS_POST = [
    (article, 'Статья'),
    (news, 'Новость')
]


class Post(models.Model):
    """
    Эта модель должна содержать в себе статьи и новости, которые создают пользователи.---
    Каждый объект может иметь одну или несколько категорий.???
    Соответственно, модель должна включать следующие поля:
    category_type поле с выбором — «статья» или «новость»
    author связь «один ко многим» с моделью Author
    data_creations автоматически добавляемая дата и время создания
    post_category связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);ok
    title заголовок статьи/новости
    rating рейтинг статьи/новости
    """

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category_type = models.CharField(max_length=2, choices=OPTIONS_POST)
    data_creations = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=150)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        """
        -like() увеличивает рейтинг на единицу.
        """
        self.rating += 1
        self.save()

    def dislike(self):
        """
        -dislike() уменьшает рейтинг на единицу.
        """
        self.rating -= 1
        self.save()

    def preview(self):
        """
        preview() модели Post, который возвращает начало статьи
        (предварительный просмотр) длиной 124 символа и добавляет многоточие в конце.
        """
        return self.text[:124] + '...'

    def __str__(self):
        dataf = 'Новость от {}'.format(self.data_creations.strftime('%d.%m.%Y %H:%M'))
        return f"{dataf}, {self.author}, {self.title}, {self.category_type}, {self.rating}"

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(args, **kwargs)
        cache.delete(f'news-{self.pk}')


class PostCategory(models.Model):
    post = models.ForeignKey('Post', null=True,on_delete=models.SET_NULL)
    in_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    """
    Модель Comment
    Под каждой новостью/статьёй можно оставлять комментарии, поэтому необходимо организовать их способ хранения тоже.
    Модель будет иметь следующие поля:
    comment_post связь «один ко многим» с моделью Post
    user_post связь «один ко многим» со встроенной моделью User (комментарии может оставить любой пользователь, необязательно автор);ok
    text текст комментария
    data_creation дата и время создания комментария
    comment_rating рейтинг комментария
    """
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_post = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    data_creation = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        """
        - like()    который увеличивает рейтинг на единицу.
        """
        self.comment_rating += 1
        self.save()

    def dislike(self):
        """
        - dislike() который уменьшают рейтинг на единицу.
        """
        self.comment_rating -= 1
        self.save()

    def __str__(self):
        return f"{self.data_creation}, {self.user_post}"
