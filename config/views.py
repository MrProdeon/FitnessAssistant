from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            rows = []
            for name in user.PROFILE_FIELDS:
                field = user._meta.get_field(name)
                if field.choices:
                    value = getattr(user, f"get_{name}_display")()
                else:
                    value = getattr(user, name)
                rows.append({"name" : name, "label" : field.verbose_name, "value" : value})
            context["profile_rows"] = rows

        return context
