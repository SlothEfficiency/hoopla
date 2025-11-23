#!/usr/bin/env python3

import argparse
import json
from string_operations import handle_string
from matching import is_it_a_match
from inverted_index import InvertedIndex


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    build_parser = subparsers.add_parser("build", help="Build an index search dictionary for faster future searches")

    args = parser.parse_args()

    #read movies
    with open("data/movies.json", "r") as f:
        movies = json.load(f)["movies"]


    match args.command:
        case "search":
            searchterm = args.query
            print(f"Searching for: {searchterm}")
            # Searching...
            inverted_index = InvertedIndex()
            inverted_index.load()
            
            search_result = []

            for token in handle_string(searchterm):
                search_result += inverted_index.get_documents(token)
                if len(search_result) >= 5:
                    break

            # Printing search results
            for i in range(0,min(5, len(search_result))):
                print(f"{i+1}: ID: {search_result[i]}, Title: {inverted_index.get_title_by_id(search_result[i])}")

        case "build":
            inverted_index = InvertedIndex()
            inverted_index.build(movies)
            inverted_index.save()
        case _:
            parser.print_help()




if __name__ == "__main__":
    main()