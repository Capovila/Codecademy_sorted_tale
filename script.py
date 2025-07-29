import utils
import sorts
import time

bookshelf = utils.load_books('books_small.csv')
bookshelf_v1 = bookshelf
bookshelf_v2 = bookshelf

long_bookshelf = utils.load_books('books_large.csv')


def by_title_ascending(a, b):
  if(a['title_lower'][0] > b['title_lower'][0]):
    return True
  return False

def by_author_ascending(a, b):
  if(a['author_lower'][0] > b['author_lower'][0]):
    return True
  return False

def by_total_length(a, b):
  if(len(a['title_lower']) + len(a['author_lower']) > 
    len(b['title_lower']) + len(b['author_lower'])):
    return True
  return False

#Print necessary time to run each sort by:
# start = time.time()
# qk_sort_long_1 = sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)
# end = time.time()
# print(f"Quicksort took {end - start:.2f} seconds"

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
qk_sort_1 = sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

sort_long_1 = sorts.bubble_sort(long_bookshelf, by_total_length)
qk_sort_long_1 = sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)

# Print authors/title to verify sorting in each sort
# for book in bookshelf_v2:
#   print(book['author_lower'])


