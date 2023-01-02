Requirements:
python3
snscrape (run `pip install snscrape`)


Use this script by creating a keyboard shortcut to run `run.sh`, or by running run.sh from your terminal.

Copy a tweet url to your clipboard before doing so, as `run.sh` will read it from your clipboard.

Feel free to change the browser configured in `config.json`, which is opened using subprocess.run(). It is currently set to `brave-browser`. E.g. for google chrome the command is `google-chrome`.

If the clipboard reading mechanism in `run.sh` doesn't work, feel free to call `run.sh` directly with the tweet url or id as a command line argument.

The script produces the conversation formatted as both markdown (in `output.md`) and html.
`output.json` is only intended to be used internally.

The path of the folder where the html file is stored can be configured in `config.json`.
You can also specify the url of said html file folder, so that the link opened in the browser is derived from said url.

If you do not host the folder at a url, leave the `htmlFolderUrl` setting in `config.json` blank.

Todo: see `TODO.md`