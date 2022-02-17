from re import template
from django.views.generic import TemplateView


class IndexView(TemplateView):
  template_name = "index.html"

  def get_context_data(self):
    cxtx = super().get_context_data()
    cxtx["username"] = "Shoya"
    return cxtx

class AboutView(TemplateView):
  template_name = "about.html"

  def get_context_data(self):
    cxtx = super().get_context_data()
    cxtx["num_services"] = "12345678"
    cxtx["skills"] = [
      "Python",
      "Javascript",
      "C++",
      "Rust",
      "Go",
    ]
    return cxtx