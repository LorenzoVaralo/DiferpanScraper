# DiferpanScraper
Web Scraping spider for extracting lots of information about each product in the paintings department of the Diferpan company website.


Diferpan is a Construction products dristibuitor of Rio Grande do Sul, Brasil. I built this project alone as a job for a Painting Store, so at first I was not intending to make it public, but with the consent of the store owner I was able to post it in this repo.

This project works for extracting information of hundreds of products of the Diferpan's Website, but unfortunatelly it lacks speed due to the Selenium module, which was not intended for web scraping but I decided to use it for its simplicity and visual verbose.

Chances are you will not be able to run the code because a business account is needed to have access to the information of products, also it is necessary to have the apropriate modules and Chrome Driver updated for the current version of Chrome.

The ExampleOutput excel file demonstrates how the information of each product is laid at the output file of the scraper, the contents of this file are edited to display false numbers for obvious reasons. The actual output excel file will have more than 1600 rows of unique products in alphabetical order, each containing the info of the example files columns, this data can be used to easily post new products in a e-commerce store.

To have acces to the website, you need to insert the email and password as an input when you first open the python file, and this information will be saved in the user.txt in the first and second line for later use.
