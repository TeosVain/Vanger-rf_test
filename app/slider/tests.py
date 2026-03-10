from django.test import TestCase
from django.urls import reverse


class SliderPageTests(TestCase):
    def test_slider_page_renders(self):
        response = self.client.get(reverse("slider-page"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Фотографии")
