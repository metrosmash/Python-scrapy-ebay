# Ebay Scraper using scrapy and residential proxy 
base code to scrape Ebay product listings utilising scrapy and residential proxies. 

# Prerequisites
To get started install scrapy using methods provided in thier documentation. [Check here for more information](https://docs.scrapy.org/en/latest/intro/install.html)
 
 For more understanding check out the youtube tutorial. [here](https://www.youtube.com/playlist?list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t)
 # Authentication & Proxy setup
 Once you have an active subscription take note of the ip address,port,username and password.
 
 Navigate to middlewares.py in `/ebay/ebay/` folder and modify the following lines to authenticate and setup the proxy.
 
```
 request.meta["proxy"] = "IP Address:Port"
        dict = {
                "User": "Username",
                "Passw": "Password"}
```

replacing IP Address, Port with the ip address of the proxy and also filling the username  with the proxy username and the password with the proxy password

# Running the scraper

Navigate to the project folder and run the following command.

```
scrapy crawl ebay
```

# Results
to save the results into a csv file run the following command. 

```
scrapy crawl ebay -o filename.csv
```

