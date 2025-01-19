# Web scraping project for jobs
This project is a web scraping application built using Flask that collects job postings from various sources. The goal is to extract data about jobs, including titles, company names, locations, and descriptions, from multiple job listing websites.

## Features

- Scrape job listings from multiple websites
- Extract job title, company, location, salary, and job description


The web scraping process involves visiting job listing websites, collecting the relevant job information, and storing it in a structured format. This project aims to automate the extraction of job-related data, enabling easy access for further processing or analysis.




## Tech

- [Flask] - A Python web framework for building the web app.
- [BeautifulSoup] - For parsing HTML and extracting job data from webpages.
- [Requests] - For sending HTTP requests to fetch web pages.
- [HTML] - Standard markup language for creating web pages.
- [TailwindCSS] - Utility-first CSS framework for creating modern designs.
- [JavaScript] - Programming language for client-side.


And of course my application is open source with a [public repository][dill]
 on GitHub.

## Installation

My application requires :

Install flask:

```sh
 pip install Flask
```

Install selenium

```sh
pip install selenium
```

WebDriver Manager: Automatically manages the driver for Selenium 

```sh
pip install webdriver-manager
```

Install Beautifulsoup4

```sh
pip install beautifulsoup4
```

Install flask-cors

```sh
pip install flask-cors
```

Install lxml

```sh
pip install lxml
```


#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
