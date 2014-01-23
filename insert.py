from crud.models import Book
import sys

Book.objects.all().delete()

# this is line
# thi si line 2


for line in sys.stdin.readlines():
	author, title = line.strip().split(",", 2)
	Book(author=author, title=title).save()
	print "%s, %s written" % (author, title)

for row in Book.objects.all():
	print row.author , row.title

