Requirements:
python3
snscrape (run `pip install snscrape`)


Use this script by creating a keyboard shortcut to run `run.sh`, or by running run.sh from your terminal.

Copy a tweet url to your clipboard before doing so, as `run.sh` will read it from your clipboard.

Feel free to change the browser configured at the end of the python script, which is opened using subprocess.run(). It is currently set to `brave-browser`.

If the clipboard reading mechanism in `run.sh` doesn't work, feel free to call main.py directly with the tweet url or id as an argument.

The script produces the conversation formatted as both markdown (in `output.md`) and html (in `output.html`).
`output.json` is only intended to be used internally.

