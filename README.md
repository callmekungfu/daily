# brightspace-downloader
Utility for downloading files from Brightspace (does not work)

## Project Status (Closed)
After repeated investigation and experimentation, the project is now concluded with a lack of success. There are far too many obstacles and difficulties to overcome, here is a summary of my findings.

The project started off smoothly, getting pass the Active Directory system wasn't that difficult of a task; however, trouble started emerging when it's time to actually start processing the logged in pages - BrightSpace is built on ajax principles. This means that most of useful content is "lazy loaded" to the user, this is great for an average user, however not so much for a spider. The ajax system combined with the fact that ever course has very different structure made the overall crawling very difficult, in the end it is simply not worth the effort to crawl BrightSpace as hand downloading each file will probably be faster.