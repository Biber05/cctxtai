from pathlib import Path
from typing import Dict, AnyStr, List

import pandas as pd

RAW_DIR = Path.cwd().joinpath("data").joinpath("00_raw").joinpath("harry_potter")
TRANFORMED_DIR = Path.cwd().joinpath("data").joinpath("10_transformed").joinpath("harry_potter")


def run():
    chapters_lookup = _read_chapters()
    chapters_lookup['Title'] = chapters_lookup['Title'].str.upper()
    chapters_lookup["Title"] = chapters_lookup["Title"].apply(lambda x: x + " \n")

    print(chapters_lookup.head())

    books = list(RAW_DIR.glob("*.txt"))
    books.sort()

    for book_idx, book in enumerate(books):
        print(f"Book: {book}")
        # chapter_names = list(chapters_lookup.loc[chapters_lookup["Book"] == book_idx + 1]["Title"])
        # chapter_names = list(map(lambda x: x + " \n", chapter_names))
        # print(f"Chapter_Names: {chapter_names}")
        with open(RAW_DIR.joinpath(book).__str__(), "r") as file:
            lines = file.readlines()

        chapters: Dict[AnyStr, List[AnyStr]] = _split_into_chapters(lines, chapters_lookup)
        for name, text in chapters.items():
            with open(TRANFORMED_DIR.joinpath(f"{name}.txt"), "w") as out:
                out.writelines(text)


def _split_into_chapters(lines: [str], chapters_lookup: pd.DataFrame) -> Dict[AnyStr, List[AnyStr]]:
    print(f"#Lines: {len(lines)}")
    lines = list(filter(lambda x: x != "\n", lines))
    print(f"#Lines after carriage return filter: {len(lines)}")
    lines = list(filter(lambda x: "Page | " not in x, lines))
    print(f"#Lines after removing page indicators: {len(lines)}")

    result: Dict[AnyStr, List[AnyStr]] = dict()
    current_chapter = ""

    for i, line in enumerate(lines):
        if line in chapters_lookup["Title"].tolist():
            chapter = list(chapters_lookup.loc[chapters_lookup["Title"] == line].values)[0]
            current_chapter = f"{chapter[0]}_{chapter[1]}"
            result[current_chapter] = [chapter[2]]
        elif current_chapter != "":
            result[current_chapter].append(line)

    return result


def _read_chapters() -> pd.DataFrame:
    return pd.read_csv(RAW_DIR.joinpath("chapters.csv").__str__(), sep=";")


if __name__ == '__main__':
    run()
