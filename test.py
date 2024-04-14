from newsplease import NewsPlease


'''
Attributes Json Example
{
  "authors": [],
  "date_download": null,
  "date_modify": null,
  "date_publish": "2017-07-17 17:03:00",
  "description": "Russia has called on Ukraine to stick to the Minsk peace process [news-please will extract the whole text but in this example file we needed to cut off here because of copyright laws].",
  "filename": "https%3A%2F%2Fwww.rt.com%2Fnews%2F203203-ukraine-russia-troops-border%2F.json",
  "image_url": "https://img.rt.com/files/news/31/9c/30/00/canada-russia-troops-buildup-.si.jpg",
  "language": "en",
  "localpath": null,
  "source_domain": "www.rt.com",
  "maintext": "Russia has called on Ukraine to stick to the Minsk peace process [news-please will extract the whole text but in this example file we needed to cut off here because of copyright laws].",
  "title": "Moscow to Kiev: Stick to Minsk ceasefire, stop making false \u2018invasion\u2019 claims",
  "title_page": null,
  "title_rss": null,
  "url": "https://www.rt.com/news/203203-ukraine-russia-troops-border/"
}
'''

article = NewsPlease.from_url(
    'https://matduggan.com/why-cant-my-mom-email-me/')
print(article)
print(article.title)
print(article.authors)
print(article.date_publish)
print(article.maintext)