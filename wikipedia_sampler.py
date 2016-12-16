import os
import sys
import getopt
import requests
import itertools
import pandas as pd

def main(title=None, save=None, cutoff=25000):
    root_article = title
    save_path = save
    cutoff_limit = cutoff

    if root_article is None:
        print 'Must provide a Wikipedia article title'
        sys.exit(2)

    endpoint = 'https://en.wikipedia.org/w/api.php'
    payload = {
        'action': 'query',
        'list': 'search',
        'format': 'json',
        'srlimit': 500,
        'srprop': 'timestamp',
        'sroffset': 0,  # use for pagination
        'srsearch': 'morelike:{}'.format(root_article),
    }

    if save_path is not None:
        save_path = os.path.join(save_path, '{}.csv'.format(root_article))
        if os.path.exists(save_path):
            # No need to query Wikipedia
            titles = pd.read_csv(save_path, header=None, index_col=0)
        else:
            titles = search_wikipedia(params=payload, cutoff=cutoff_limit)
            titles.to_csv(save_path, encoding="utf-8")
    else:
        titles = search_wikipedia(params=payload, cutoff=cutoff_limit)

    # Sample articles, reducing the weight of articles further down the list
    print titles.sample(
        n=5,
        weights=1.0 / (1 + titles.index)
    )

def parse_argv(argv):
    '''

    '''
    root_article = None
    save_path = None
    cutoff_limit = 25000
    try:
        opts, args = getopt.getopt(
            args=argv,
            shortopts="ht:s:c:",
            longopts=[
                "help",
                "title=",
                "save=",
                "cutoff="
            ])
    except getopt.GetoptError:
        print 'There was an error running the script. Run python wikipedia_sampler.py --help for more info'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print 'python wikipedia_sampler.py -t <article_title> -s <path_to_saved_articles> -c <cutoff_limit>'
            print '-t or --title: Title of the root wikipedia article. Grab this from the URL. Example: Educational_Technology'
            print '-s or --save (optional): Directory at which to load and/or save articles that are related to --title. This will significantly speed up the script for future runs'
            print '-c or --cutoff (optional): Number of related articles to pull from Wikipedia'
            sys.exit()
        if opt in ("-t", "--title"):
            root_article = arg
        if opt in ("-s", "--save"):
            save_path = arg
        if opt in ("-c", "--cutoff"):
            cutoff_limit = int(arg)

    return (root_article, save_path, cutoff_limit)


def search_wikipedia(params, cutoff):
    '''
    Returns a Pandas Series of wikipedia article titles
    '''
    payload = params
    cutoff_limit = cutoff
    # Initialize variables for while loop
    out = {'continue': None}  # existence of this key dictates whether to keep looping
    articles = []
    # Paginate through Wikipedia's related articles
    while 'continue' in out and payload['sroffset'] <= cutoff_limit:
        r = requests.get(endpoint, params=payload)
        out = r.json()  # decode JSON output
        articles.append(out['query']['search'])
        if 'continue' in out:
            payload['sroffset'] = out['continue']['sroffset']
    # Re-format related articles into Pandas series
    titles = pd.Series([(article['title']) for article in itertools.chain.from_iterable(articles)])
    return titles

if __name__ == '__main__':
    main(*parse_argv(sys.argv[1:]))
