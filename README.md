Requirements:
```
sudo apt-get install xdg-utils xsel python3 python3-pip
pip install snscrape 
```


Use this script by creating a keyboard shortcut to execute `run.sh`, or by executing `run.sh` directly from your terminal.

`run.sh` will download the conversation for a tweet id or url either given to it as a command line argument, or which is selected/highlighted in another application.

If the clipboard reading mechanism used by `run.sh` doesn't work, `run.sh` can be called directly with the tweet url or id as a command line argument.

e.g.  
```./run.sh https://twitter.com/evoskuil/status/1356279556924080128```

The script produces the conversation formatted as both markdown (in `output.md`) and as html.

The path of the folder where the html file is stored can be configured in `config.json`.

You can also specify the url of said html file folder, which will be used when opening the html file in the browser.
If you do not host the folder at a url, leave the `htmlFolderUrl` setting in `config.json` blank.

Todo: see `TODO.md`