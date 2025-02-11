import io
import math
from collections import Counter
from django.core.paginator import Paginator
from django.views import View
from django.shortcuts import render


class TFIDFView(View):
    template_name = "index.html"
    words_per_page = 10

    @staticmethod
    def calculate_tfidf(text):
        words = text.split()
        total_words = len(words)
        tf_counter = Counter(words)

        tf = {word: count / total_words for word, count in tf_counter.items()}
        idf = {word: math.log(total_words / (count + 1)) for word, count in tf_counter.items()}

        tfidf = sorted([(word, tf[word], idf[word]) for word in tf], key=lambda x: x[2], reverse=True)
        return tfidf

    def get(self, request):
        tfidf_result = request.session.get("tfidf_result")

        if tfidf_result:
            paginator = Paginator(tfidf_result, self.words_per_page)
            page_number = request.GET.get("page", 1)
            page_obj = paginator.get_page(page_number)
            return render(request, self.template_name, {"page_obj": page_obj})

        return render(request, self.template_name)

    def post(self, request):
        uploaded_file = request.FILES.get("file")
        if uploaded_file:
            text = io.TextIOWrapper(uploaded_file.file, encoding="utf-8").read()
            tfidf_result = self.calculate_tfidf(text)

            request.session["tfidf_result"] = tfidf_result

            paginator = Paginator(tfidf_result, self.words_per_page)
            page_obj = paginator.get_page(1)

            return render(request, self.template_name, {"page_obj": page_obj})

        return render(request, self.template_name)
