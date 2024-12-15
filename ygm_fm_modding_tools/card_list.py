"""
Downloads the whole card list of the game with the in-game cards picture sourcds
"""

import pandas as pd
import httpx
from bs4 import BeautifulSoup
import polars as pl
import logging
from YGO_FM_Modding_Tools.ygm_fm_modding_tools.config import DATA_FOLDER

CARD_LIST_FILE = DATA_FOLDER / "card_list.csv"


if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://google.com",
    }
    response = httpx.get(
        "https://yugipedia.com/wiki/List_of_Yu-Gi-Oh!_Forbidden_Memories_cards",
        headers=headers,
        timeout=httpx.Timeout(10.0),
    )
    soup = BeautifulSoup(response.content, "html.parser")
    card_pictures = []
    true_card_urls = []
    card_list = (
        pl.from_pandas(
            pd.read_html(str(soup.find_all("table", class_="wikitable")[0]))[0]
        )
        .drop(["Password", "SC Cost"])
        .with_columns(
            card_wiki_url="https://yugioh.fandom.com/wiki/"
            + pl.col("Card")
            .str.replace_all(" ", "_")
            .str.replace_all("#", "")
            .str.replace_all("&", "%26")
            + "_(FMR)"
        )
    )
    logging.info("Web scrapping yugioh wiki, this should takes around 5 minutes")
    for row in card_list.iter_rows(named=True):
        url = row["card_wiki_url"]
        if row["Card"] == "Winged Dragon #1":
            url = "https://yugioh.fandom.com/wiki/Winged_Dragon_1"
        elif row["Card"] == "Frog The Jam":
            url = "https://yugioh.fandom.com/wiki/Frog_the_Jam_(FMR)"
        logging.info(url)
        response = httpx.get(url, headers=headers, timeout=httpx.Timeout(10.0))
        if response is None or response.is_error or response.status_code == 301:
            url = url.removesuffix("_(FMR)")
            logging.info(f"Retry with url {url}")
            response = httpx.get(url, headers=headers, timeout=httpx.Timeout(10.0))
        soup = BeautifulSoup(response.content, "html.parser")
        card_picture = (
            soup.find(class_="cardtable-main_image-wrapper").find("img").get("src")
        )
        card_pictures.append(card_picture)
        true_card_urls.append(url)
    card_list = (
        card_list.with_columns(picture=pl.Series("picture", card_pictures))
        .drop("card_wiki_url")
        .with_columns(card_wiki_url=pl.Series("card_wiki_url", true_card_urls))
    )

    logging.info(f"Writting card list in {CARD_LIST_FILE} ")
    card_list.write_csv(CARD_LIST_FILE)
