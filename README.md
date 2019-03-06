# wikipedia-digest
Explore and discover new points of interest that are centered around a topic of your choice!

This script is meant to help you think about your topic of interest in unexpected new ways.
Maybe you're trying to come up with a business idea in education so you use this script to find Wikipedia articles that
are loosely related to education.
You end up discovering some historical figures who had a vision for education that wasn't possible before the Internet. Boom! You're in business.

It works by traversing through the links of a given Wikipedia article (as well as those links' links) and randomly samples new articles from this set. You're meant to re-run this script as many times as you want (each time will yield different results) until your Eureka moment.

## Usage
Copy the code in `wikipedia_sampler.py` and run it like in the example below. (You might get errors the first couple times if you're missing packages that you'll need to install. See `requirements.txt` for packages to install)
```
# See python wikipedia_sampler.py --help for details
python wikipedia_sampler.py --title Educational_technology --save <DIRECTORY> --cutoff 25000
```
#### Explaining the above command
`python wikipedia_sampler.py` - Run the script using the Python interpreter

`--title Educational_technology` - "Educational_technology" is the name of a Wikipedia article.
You get it by grabbing the last part of a Wikipedia URL. For example "Educational_technology" is the last part of this URL: https://en.wikipedia.org/wiki/Educational_technology.
This article will be the root from which the script will start clicking links.

`--save <DIRECTORY>` - This is optional. You can replace `<DIRECTORY>` with the path to a folder that you want to save intermediate results in. The script will use that file instead of Wikipedia's API next time around.

`--cutoff 25000` - also optional. Number of related articles to pull from Wikipedia (default is 25000)

## Example Output
The script will return five Wikipedia articles that are somehow related to your original article.

This is what one run of the example command could yield. Because the results are randomized, yours will most likely be different.
```
824     After School (app)
887            Jimmy Wales
3556            Dal Shabet
5                     Voat
4889            Pittsburgh
dtype: object
```
The first column indicates the distance of the Wikipedia article from your initial query. The farther the distance, the less "related" it is to your original root article. But who knows, maybe your brain will make a brilliant connection!

To view the article, simply paste it at the end of the wikipedia URL. **Example**: `https://en.wikipedia.org/wiki/After School (app)`

Good luck finding your Eureka moment!
