from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import category, detail, home, all_news, all_category


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)
    
    def test_list_url_is_resolved(self):
        url = reverse('all-news')
        print(resolve(url))
        self. assertEquals(resolve(url).func, all_news)
    

    def test_detail_url_is_resolved(self):
        url = reverse('detail', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, detail)
    
    def test_all_category_url_is_resolved(self):
        url = reverse('all-category')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_category)
    
    def test_category_url_is_resolved(self):
        url = reverse('category', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, category)
    