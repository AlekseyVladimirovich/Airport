from django.db import models


class Arriving(models.Model):
	boardNumber = models.CharField(max_length=150, db_index=True)
	from_at = models.CharField(max_length=150, db_index=True)
	startTime = models.CharField(max_length=150, db_index=True)
	to = models.CharField(max_length=150, db_index=True)
	endTime = models.CharField(max_length=150, db_index=True)
	status = models.CharField(max_length=150, db_index=True)

	def __str__(self):
		return '{}'.format(self.boardNumber)