# wikipedia-digest
Explore and discover new points of interest that are centered around a topic of your choice!

This script traverses through the links of a given Wikipedia article (as well as those links' links) and randomly samples new articles from this set. The shorter the link distance between a traversed article and the original, the more likely it will be selected by the sampler (however the sheer number of articles that are farther away will ensure their representation).

## Usage
```
# See python wikipedia_sampler.py --help for details
python wikipedia_sampler.py --title Educational_Technology --save <DIRECTORY> --cutoff 25000
```
