import argparse
import json
import random

from src.common.utils import Post


def import_data(file: str):
    with open(file) as fp:
        return json.load(fp)


def parse_args() -> tuple[str, str, int]:
    parser = argparse.ArgumentParser(
        description="Extract json file to tsv",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("-o", help="Output file", type=str, default="output.tsv")
    parser.add_argument(
        "input_file",
        help="The json file to be converted",
    )
    parser.add_argument("posts", help="The number of random posts", type=int)

    args = parser.parse_args()

    return args.o, args.input_file, args.posts


def add_posts_to_tsv(output: str, posts: list[Post]):
    with open(output, "w", newline="") as tsvfile:
        tsvfile.write("Name\ttitle\tcoding\n\n")
        for post in posts:
            tsvfile.write(f"{post.name}\t{post.text}\t\n")


def select_random(num_posts: int, posts) -> list[Post]:
    print(num_posts)
    posts = posts if num_posts >= len(posts) else random.sample(posts, num_posts)
    post_list = []
    for post in posts:
        post_data = post["data"]
        post_text = post_data["title"]
        post_name = post_data["name"]
        post_item = Post()
        post_item.text = post_text
        post_item.name = post_name
        post_list.append(post_item)

    return post_list


def main():
    output, input, num_posts = parse_args()

    json_data = import_data(input)

    posts = json_data["data"]["children"]

    post_list = select_random(num_posts, posts)

    add_posts_to_tsv(output, post_list)

    pass


if __name__ == "__main__":
    main()
