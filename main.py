import snscrape.modules.twitter as sntwitter
import subprocess
import json
import sys

headHtml = """
<head>
  <style>
    html {
        background-color: black;
        color: white;
    }
      .indent {
        padding-left: 20px;
        margin-left: 20px;
        border: 1px solid white;

      }
    li {
      margin: 0;
      padding: 5px;
    }
  </style>
</head>"""


def get_first_arg():
    # sys.argv is a list that contains the command-line arguments
    # The first element of the list (sys.argv[0]) is the name of the script itself
    # The second element (sys.argv[1]) is the first argument, and so on
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return None


def get_replies(tweet_id):
    replies_dict = {}
    # Set the conversation_id search parameter to the tweet ID
    scraper = sntwitter.TwitterSearchScraper(
        "conversation_id:" + tweet_id + " (filter:safe OR -filter:safe)"
    )
    mainTweet = sntwitter.TwitterTweetScraper(
        tweet_id, mode=sntwitter.TwitterTweetScraperMode.RECURSE
    ).get_items()
    tweets = [tweet for tweet in scraper.get_items()]
    tweets.extend(mainTweet)
    # Iterate through the replies to the tweet using the scraper
    for reply in tweets:
        # Add the reply to the dictionary structure
        text = "[" + reply.user.username + "] : " + reply.content.replace("\n", "  ")
        if reply.id in replies_dict:
            replies_dict[reply.id]["text"] = text
        else:
            replies_dict[reply.id] = {"text": text, "children": []}
        # If the reply has a parent tweet, add it as a child to the parent tweet in the dictionary structure
        if reply.inReplyToTweetId:
            parent_id = reply.inReplyToTweetId
            if parent_id in replies_dict:
                replies_dict[parent_id]["children"].append(reply.id)
                replies_dict[parent_id]["children"] = list(
                    set(replies_dict[parent_id]["children"])
                )
            else:
                replies_dict[parent_id] = {"text": "", "children": [reply.id]}

    return replies_dict


def json_to_md(json_data, topTweet):
    # Initialize an empty HTML string
    # Recursively convert each tweet and its children to HTML
    def convert_to_md(tweet_id, level):
        outStr = ""
        # Indent the tweet based on its level in the hierarchy
        indent = "    " * level + "- "
        tweet = json_data[int(tweet_id)]
        # Add the tweet text to the HTML string
        outStr = indent + tweet["text"] + "\n"
        # print(sorted(tweet["children"]), tweet_id)
        # Recursively convert the children of the tweet to HTML
        for childId in tweet["children"]:
            print(childId, "->", tweet_id)
            outStr += convert_to_md(childId, level + 1)

        return outStr

    # Convert the top-level tweets to HTML

    outStr = convert_to_md(topTweet, 0)

    return outStr


def markdown_to_html(markdown_list):
    html_output = ""
    # Initialize the indent level to 0
    indent_level = 0
    # Split the input string into lines
    lines = markdown_list.split("\n")
    for line in lines:

        # Get the number of leading spaces on the line
        leading_spaces = len(line) - len(line.lstrip())

        # Calculate the new indent level
        new_indent_level = leading_spaces // 2

        # If the new indent level is greater than the current indent level, add a new div
        if new_indent_level > indent_level:
            html_output += '<div class="indent">'

        # If the new indent level is less than the current indent level, close the current div
        elif new_indent_level < indent_level:
            html_output += "</div>"

        # Update the current indent level
        indent_level = new_indent_level

        # Add the line as a list item to the HTML
        html_output += "<li>" + line.strip() + "</li>"

    # Close any remaining open divs
    html_output += "</div>" * indent_level
    html_output = "<html>" + headHtml + "\n<body>\n" + html_output + "\n</body></html>"
    return html_output


if __name__ == "__main__":
    tweet_id = get_first_arg()
    replies = get_replies(tweet_id)
    with open("output.json", "w") as outputMdFile:
        outputMdFile.write(json.dumps(replies, indent=4))

    outputMd = json_to_md(replies, tweet_id)

    with open("output.md", "w") as outputMdFile:
        outputMdFile.write(outputMd)

    html = markdown_to_html(outputMd)

    with open("output.html", "w") as outputHtmlFile:
        outputHtmlFile.write(html)

    subprocess.run(["brave-browser", "./output.html"])
