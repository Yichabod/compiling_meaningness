## Scraping Meaningness

This is a messy attempt to put all of `meaningness.com` into a single pdf for convenient offline reading. I have asked David Chapman for permission and he granted it but said he could not endorse it because he planned to turn the websites into books. Accordingly, I'll take this repo down once he publishes the books.

In the meantime, feel free to add to this so more people can read David Chapman.


### Code notes

My ideal version has text on a white background with a table of contents at the beginning, page numbers, and images in the right places. The images have proved to be quite annoying to deal with.

weasy_scrape.py uses weasyprint and currently should get all of meaningness *without images* into a pdf. It is currently badly formatted (no table of contents, and it is hard to tell where you are in the book) but better than nothing.

Another approach is to use pdfkit and take a pdf version of each entire webpage and concatenate them together. This approach will have diagrams but takes up a lot of space because the table of contents are repeated each time. Also it looks pretty ugly.


