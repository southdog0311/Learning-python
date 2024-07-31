from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from catalog.models import Author

class AuthorViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 創建一個 Author 對象
        cls.author = Author.objects.create(
            first_name='Big',
            last_name='Bob',
            date_of_death=timezone.now()
        )

    def test_author_list_view(self):
        response = self.client.get(reverse('authors'))
        # 確保狀態碼為 200 OK
        self.assertEqual(response.status_code, 200)
        # 確保返回的 HTML 中包含作者名字
        self.assertContains(response, 'Big Bob')
        # 確保使用了正確的模板
        self.assertTemplateUsed(response, 'catalog/author_list.html')

    def test_author_detail_view(self):
        response = self.client.get(reverse('author-detail', args=[self.author.id]))
        # 確保狀態碼為 200 OK
        self.assertEqual(response.status_code, 200)
        # 確保返回的 HTML 中包含作者的詳細信息
        self.assertContains(response, 'Big Bob')
        # 確保使用了正確的模板
        self.assertTemplateUsed(response, 'catalog/author_detail.html')
