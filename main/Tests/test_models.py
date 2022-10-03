from django.test import TestCase

from main.models import Category, News


class TestModels(TestCase):
    def setUp(self):
        self.category_1 = Category.objects.create(id=1 , title="Action")
        self.news_1 = News.objects.create(title= "Deadpool", detail= "Suspense", category=self.category_1)

    

    def test_category_creation(self):

        self.assertTrue(isinstance(self.category_1,Category))
        self.assertEqual(self.category_1.__str__(), self.category_1.title)
    
    def test_news_creation(self):
        self.assertTrue(isinstance(self.news_1,News))
        self.assertEqual(self.news_1.__str__(), self.news_1.title, self.news_1.detail)
    
    def test_news1_has_a_category(self):
        self.assertEqual(self.news_1.category, self.category_1)
    
    def test_news1_is_an_action_category(self):
        self.assertTrue(isinstance(self.news_1.category,Category))

    
