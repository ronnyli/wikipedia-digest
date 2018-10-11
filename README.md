# wikipedia-digest
Explore and discover new points of interest that are centered around a topic of your choice!

This script traverses through the links of a given Wikipedia article (as well as those links' links) and randomly samples new articles from this set. The shorter the link distance between a traversed article and the original, the more likely it will be selected by the sampler (however the sheer number of articles that are farther away will ensure their representation).

## Usage
```
# See python wikipedia_sampler.py --help for details
python wikipedia_sampler.py --title Educational_Technology --save <DIRECTORY> --cutoff 25000
```

## Example Output
```
824     After School (app)
887            Jimmy Wales
3556            Dal Shabet
5                     Voat
4889            Pittsburgh
dtype: object
```
The first column indicates the distance of the Wikipedia article from your initial query. To view the wikipedia article, simply paste it at the end of the wikipedia URL. **Example**: `https://en.wikipedia.org/wiki/After School (app)`
