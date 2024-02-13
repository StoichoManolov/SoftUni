def add_songs(*args):

    result, output = {}, []
    for song, lyrics in args:
        result[song] = result.get(song, []) + lyrics

    for key, value in result.items():
        output.append(f"- {key}")
        for text in value:
            output.append(text)

    return '\n'.join(output)

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))


