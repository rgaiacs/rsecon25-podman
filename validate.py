import argparse

from lxml.html import fragment_fromstring


def validate(tree, heading, word_limit):
    capture = False
    section = []

    for node in tree:
        if node.tag.startswith("h") and node.text == heading:
            capture = True
            continue

        if capture and node.tag.startswith("h"):
            break

        if capture:
            section.append(node)

    text = "".join([paragraph.text for paragraph in section])
    number_of_words = len(text.split())

    if number_of_words > word_limit:
        print(f"{heading} exceeded the word limit! {number_of_words} > {word_limit}")


def main(tree):
    """
    Check all sections.
    """
    validate(tree, "Title", 50)
    validate(tree, "Abstract", 300)
    validate(tree, "Prerequisites", 150)
    validate(tree, "Outcomes", 150)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--filename", default="workshop-submission-form.html")

    args = parser.parse_args()

    with open(args.filename, "r") as _file:
        tree = fragment_fromstring(_file.read(), create_parent=True)
    main(tree)
