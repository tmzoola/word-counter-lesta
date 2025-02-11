import io
import math
from django.test import TestCase, Client
from django.core.paginator import Paginator
from django.urls import reverse
from collections import Counter
from word_counter.views import TFIDFView


class TFIDFViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_calculate_tfidf(self):
        text = "apple banana apple fruit banana fruit fruit"
        expected_words = ["apple", "banana", "fruit"]
        expected_tf = {
            "apple": 2 / 7,
            "banana": 2 / 7,
            "fruit": 3 / 7
        }
        expected_idf = {word: math.log(7 / (count + 1)) for word, count in Counter(text.split()).items()}


        tfidf_result = TFIDFView.calculate_tfidf(text)
        words_in_result = [word for word, _, _ in tfidf_result]

        self.assertEqual(len(tfidf_result), 3)
        self.assertListEqual(sorted(words_in_result), sorted(expected_words))
        for word, tf, idf in tfidf_result:
            self.assertAlmostEqual(tf, expected_tf[word])
            self.assertAlmostEqual(idf, expected_idf[word])

    def test_upload_file(self):
        text_content = "apple banana apple fruit banana fruit fruit"
        file = io.BytesIO(text_content.encode("utf-8"))
        file.name = "test.txt"

        response = self.client.post(reverse("tfidf_view"), {"file": file}, format="multipart")

        self.assertEqual(response.status_code, 200)
        self.assertIn("page_obj", response.context)
        self.assertGreaterEqual(len(response.context["page_obj"].object_list), 1)

    def test_session_storage(self):
        text_content = "apple apple banana fruit"
        file = io.BytesIO(text_content.encode("utf-8"))
        file.name = "test.txt"

        self.client.post(reverse("tfidf_view"), {"file": file}, format="multipart")

        session_data = self.client.session.get("tfidf_result")
        self.assertIsNotNone(session_data)
        self.assertGreaterEqual(len(session_data), 1)

    def test_pagination(self):
        text_content = " ".join(f"word{i}" for i in range(100))
        file = io.BytesIO(text_content.encode("utf-8"))
        file.name = "test.txt"

        self.client.post(reverse("tfidf_view"), {"file": file}, format="multipart")

        response = self.client.get(reverse("tfidf_view") + "?page=1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("page_obj", response.context)

        paginator = Paginator(self.client.session.get("tfidf_result"), TFIDFView.words_per_page)
        self.assertEqual(len(response.context["page_obj"].object_list), paginator.per_page)
