from django.db import models


class WishList(models.Model):
    user = models.ForeignKey(
        "account.User", on_delete=models.CASCADE, related_name="wish_list", verbose_name="Foydalanuvchi"
    )
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE, verbose_name="Kitob")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Saqlangan"
        verbose_name_plural = "Saqlanganlar"
        unique_together = ["user", "book"]

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
