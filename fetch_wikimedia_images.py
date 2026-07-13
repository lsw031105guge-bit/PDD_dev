#!/usr/bin/env python3
import json
import os
import random
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
import shutil


API = "https://commons.wikimedia.org/w/api.php"
SSL_CONTEXT = ssl._create_unverified_context()
USER_AGENT = "PDDDevBot/1.0 (https://github.com/lsw031105guge-bit/PDD_dev)"


def http_get_json(url: str):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json,text/plain,*/*",
        },
    )
    with urllib.request.urlopen(req, timeout=20, context=SSL_CONTEXT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def safe_mkdir(path: str):
    os.makedirs(path, exist_ok=True)


def search_files(keyword: str, limit: int):
    params = {
        "action": "query",
        "list": "search",
        "srsearch": keyword,
        "srnamespace": "6",
        "srlimit": str(limit),
        "format": "json",
    }
    url = f"{API}?{urllib.parse.urlencode(params)}"
    data = http_get_json(url)
    return [item["title"] for item in data.get("query", {}).get("search", [])]


def get_thumb_url(file_title: str, width: int):
    params = {
        "action": "query",
        "titles": file_title,
        "prop": "imageinfo",
        "iiprop": "url|extmetadata",
        "iiurlwidth": str(width),
        "format": "json",
    }
    url = f"{API}?{urllib.parse.urlencode(params)}"
    data = http_get_json(url)
    pages = data.get("query", {}).get("pages", {})
    for _, page in pages.items():
        info = (page.get("imageinfo") or [None])[0]
        if not info:
            continue
        return info.get("thumburl") or info.get("url"), info.get("extmetadata") or {}
    return None, {}


def slugify(s: str):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s or "item"


def download(url: str, out_path: str):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=40, context=SSL_CONTEXT) as resp:
        content = resp.read()
    with open(out_path, "wb") as f:
        f.write(content)


def pick_unique_titles(titles, used, want):
    random.shuffle(titles)
    picked = []
    for t in titles:
        if t in used:
            continue
        used.add(t)
        picked.append(t)
        if len(picked) >= want:
            break
    return picked


def main():
    random.seed(42)

    base_dir = os.path.join(os.path.dirname(__file__), "docs", "images")
    safe_mkdir(base_dir)

    categories = [
        ("slippers", "slippers product photo"),
        ("socks", "socks product photo"),
        ("keyboard", "computer keyboard product photo"),
        ("mirror", "full length mirror product photo"),
        ("cat_bed", "cat bed product photo"),
        ("umbrella", "umbrella product photo"),
        ("humidifier", "desktop humidifier product photo"),
        ("projector", "mini projector product photo"),
        ("mouse_pad", "mouse pad product photo"),
        ("alarm_clock", "digital alarm clock product photo"),
    ]

    used_titles = set()
    records = []

    for folder, keyword in categories:
        out_dir = os.path.join(base_dir, folder)
        safe_mkdir(out_dir)

        titles = search_files(keyword, limit=25)
        picked = pick_unique_titles(titles, used_titles, want=3)
        if len(picked) < 3:
            print(f"[warn] {folder}: only found {len(picked)} files for keyword={keyword}", file=sys.stderr)

        downloaded = 0
        for idx, file_title in enumerate(picked, start=1):
            url, meta = get_thumb_url(file_title, width=900)
            if not url:
                print(f"[warn] no url for {file_title}", file=sys.stderr)
                continue
            if not re.search(r"\.(jpe?g)(\?|$)", url, re.IGNORECASE):
                print(f"[warn] skip non-jpeg thumburl for {file_title}: {url}", file=sys.stderr)
                continue

            out_path = os.path.join(out_dir, f"{idx:03d}.jpg")
            download(url, out_path)
            downloaded += 1
            time.sleep(0.3)

            license_name = (meta.get("LicenseShortName") or {}).get("value") if isinstance(meta, dict) else None
            artist = (meta.get("Artist") or {}).get("value") if isinstance(meta, dict) else None
            source = (meta.get("ImageDescription") or {}).get("value") if isinstance(meta, dict) else None

            records.append(
                {
                    "category": folder,
                    "file": f"docs/images/{folder}/{idx:03d}.jpg",
                    "commons_title": file_title,
                    "commons_file_page": f"https://commons.wikimedia.org/wiki/{urllib.parse.quote(file_title.replace(' ', '_'))}",
                    "license": license_name,
                    "artist": artist,
                    "note": source,
                }
            )

        if downloaded and downloaded < 3:
            last = os.path.join(out_dir, f"{downloaded:03d}.jpg")
            for idx in range(downloaded + 1, 4):
                out_path = os.path.join(out_dir, f"{idx:03d}.jpg")
                shutil.copyfile(last, out_path)

    out_meta = os.path.join(os.path.dirname(__file__), "docs", "IMAGE_SOURCES.json")
    with open(out_meta, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

    print("done")


if __name__ == "__main__":
    main()
