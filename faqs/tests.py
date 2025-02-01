from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python web framework."
        )

    def test_translation(self):
        """Check if translations are generated"""
        self.assertEqual(self.faq.get_translation('en'), self.faq.question)
        self.assertIsNotNone(self.faq.question_hi)
        self.assertIsNotNone(self.faq.question_bn)

    def test_faq_creation(self):
        """Ensure FAQ object is created correctly"""
        self.assertEqual(str(self.faq), "What is Django?")
