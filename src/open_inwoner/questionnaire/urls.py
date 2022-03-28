from django.urls import path

from open_inwoner.questionnaire.views import (
    QuestionnaireExportView,
    QuestionnaireResetView,
    QuestionnaireStepView,
)

app_name = "questionnaire"

urlpatterns = [
    path("reset", QuestionnaireResetView.as_view(), name="reset"),
    path("<str:slug>", QuestionnaireStepView.as_view(), name="root_step"),
    path(
        "<str:root_slug>/<str:slug>",
        QuestionnaireStepView.as_view(),
        name="descendent_step",
    ),
    path("", QuestionnaireStepView.as_view(), name="index"),
    path("export/", QuestionnaireExportView.as_view(), name="questionnaire_export"),
]
