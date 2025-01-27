# 문장에서 공백을 기준으로 단어의 개수를 출력
import re
from builtins import list
from typing import Any

sentence = 'suppose we have few words that are separated by space'


# 파일 읽기

def read_file1(path: str) -> list[Any]:
    with open(path, "r") as file:
        txt: str = file.read()
    txt = txt.replace(",", " ")
    return txt.split()


def read_file2(path: str) -> list[Any]:
    with open(path, "r") as file:
        txt: str = file.read()
    return re.split(" |,", txt)


def read_and_write_to_upper(path: str) -> None:
    with open(path, "r") as read_file:
        txt: str = read_file.read()
        upper_text = txt.upper()
    with open(path, "w") as append_file:
        append_file.write(upper_text)


if __name__ == "__main__":
    print(
        sentence.split().__len__()
    )

    b = input()
    print(
        b.split("&").__len__()
    )

    print(
        read_file1("./dictionary.py")
    )

    print(
        read_file2("./dictionary.py")
    )

    read_and_write_to_upper("./dictionary.py")

    print(
        read_file1("./dictionary.py")
    )