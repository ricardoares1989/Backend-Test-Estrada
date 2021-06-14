from django.db import models


class TimeStampedModel(models.Model):
    """Model with default fields, abstract based, for give
    other models the timestamped data.
    Args:
        created_at(Datetime): store the dateimte the object was created.
        updated_at(Datatime): store the last modification of the object.
    """

    created_at = models.DateTimeField(
        "created at",
        auto_now_add=True,
        help_text="Date time on which the object was created.",
    )
    updated_at = models.DateTimeField(
        "updated at",
        auto_now=True,
        help_text="Date time on which the object was modified",
    )

    class Meta:
        """Meta options."""

        abstract = True
        get_latest_by = "created_at"
        ordering = ["-created_at", "-updated_at"]
