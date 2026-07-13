#!/usr/bin/env bash
set -euo pipefail

BASE="https://coresg-normal.trae.ai/api/ide/v1/text_to_image"
SIZE="square"
PLACEHOLDER_SHA256="e330cd023298a812503e10a067a3f88e1cbc094f37f6fd2a88fdb6799495b37e"
MAX_RETRY=40
SLEEP_SECONDS=2

gen () {
  local out="$1"
  local prompt="$2"
  local i=1
  while true; do
    curl -L -G "$BASE" --data-urlencode "prompt=${prompt}" --data-urlencode "image_size=${SIZE}" -o "$out"
    local sha
    sha="$(shasum -a 256 "$out" | awk '{print $1}')"
    if [[ "$sha" != "$PLACEHOLDER_SHA256" ]]; then
      break
    fi
    if [[ "$i" -ge "$MAX_RETRY" ]]; then
      echo "failed to generate image (still placeholder): $out" >&2
      break
    fi
    sleep "$SLEEP_SECONDS"
    i=$((i+1))
  done
}

mkdir -p docs/images/{slippers,socks,keyboard,mirror,cat_bed,umbrella,humidifier,projector,mouse_pad,alarm_clock}

gen docs/images/slippers/001.jpg "realistic ecommerce product photo of home slippers, white background, studio lighting, Chinese online shopping style, highly realistic, no text, no logo, product centered"
gen docs/images/slippers/002.jpg "realistic ecommerce product photo of home slippers, white background, studio lighting, Chinese online shopping style, highly realistic, no text, no logo, slight angle"
gen docs/images/slippers/003.jpg "realistic ecommerce product photo of home slippers, white background, studio lighting, Chinese online shopping style, highly realistic, no text, no logo, close-up detail"

gen docs/images/socks/001.jpg "realistic ecommerce product photo of socks, white background, studio lighting, Chinese online shopping style, highly realistic, no text, no logo, product centered"
gen docs/images/socks/002.jpg "realistic ecommerce product photo of socks, white background, studio lighting, Chinese online shopping style, highly realistic, no text, no logo, slight angle"
gen docs/images/socks/003.jpg "realistic ecommerce product photo of socks, white background, studio lighting, Chinese online shopping style, highly realistic, no text, no logo, close-up texture"

gen docs/images/keyboard/001.jpg "realistic ecommerce product photo of office keyboard, clean commercial lighting, Chinese online shopping style, highly realistic, no text, no logo, product centered"
gen docs/images/keyboard/002.jpg "realistic ecommerce product photo of office keyboard, clean commercial lighting, Chinese online shopping style, highly realistic, no text, no logo, slight angle"
gen docs/images/keyboard/003.jpg "realistic ecommerce product photo of office keyboard, clean commercial lighting, Chinese online shopping style, highly realistic, no text, no logo, close-up keys"

gen docs/images/mirror/001.jpg "realistic ecommerce product photo of a full length mirror, small apartment corner, natural light, highly realistic, no text, no logo"
gen docs/images/mirror/002.jpg "realistic ecommerce product photo of a full length mirror, small apartment corner, natural light, highly realistic, no text, no logo, slight angle"
gen docs/images/mirror/003.jpg "realistic ecommerce product photo of a full length mirror, minimal room, highly realistic, no text, no logo"

gen docs/images/cat_bed/001.jpg "realistic ecommerce product photo of soft cat bed, pet supplies product shot, clean white background, highly realistic, no text, no logo"
gen docs/images/cat_bed/002.jpg "realistic ecommerce product photo of soft cat bed, pet supplies product shot, clean white background, highly realistic, no text, no logo, slight angle"
gen docs/images/cat_bed/003.jpg "realistic ecommerce product photo of soft cat bed, pet supplies product shot, clean white background, highly realistic, no text, no logo, close-up detail"

gen docs/images/umbrella/001.jpg "realistic ecommerce product photo of transparent umbrella, studio product shot, white background, highly realistic, no text, no logo"
gen docs/images/umbrella/002.jpg "realistic ecommerce product photo of transparent umbrella, studio product shot, white background, highly realistic, no text, no logo, slight angle"
gen docs/images/umbrella/003.jpg "realistic ecommerce product photo of transparent umbrella, studio product shot, white background, highly realistic, no text, no logo, close-up detail"

gen docs/images/humidifier/001.jpg "realistic ecommerce product photo of a small desktop humidifier, clean background, highly realistic, no text, no logo, product centered"
gen docs/images/humidifier/002.jpg "realistic ecommerce product photo of a small desktop humidifier, clean background, highly realistic, no text, no logo, slight angle"
gen docs/images/humidifier/003.jpg "realistic ecommerce product photo of a small desktop humidifier, clean background, highly realistic, no text, no logo, close-up detail"

gen docs/images/projector/001.jpg "realistic ecommerce product photo of mini projector, consumer electronics product shot, clean background, highly realistic, no text, no logo"
gen docs/images/projector/002.jpg "realistic ecommerce product photo of mini projector, consumer electronics product shot, clean background, highly realistic, no text, no logo, slight angle"
gen docs/images/projector/003.jpg "realistic ecommerce product photo of mini projector, consumer electronics product shot, clean background, highly realistic, no text, no logo, close-up detail"

gen docs/images/mouse_pad/001.jpg "realistic ecommerce product photo of heated mouse pad on desk, electronics accessory product photo, highly realistic, no text, no logo"
gen docs/images/mouse_pad/002.jpg "realistic ecommerce product photo of heated mouse pad on desk, electronics accessory product photo, highly realistic, no text, no logo, slight angle"
gen docs/images/mouse_pad/003.jpg "realistic ecommerce product photo of heated mouse pad on desk, electronics accessory product photo, highly realistic, no text, no logo, close-up detail"

gen docs/images/alarm_clock/001.jpg "realistic ecommerce product photo of digital alarm clock on bedside table, clean background, highly realistic, no text, no logo"
gen docs/images/alarm_clock/002.jpg "realistic ecommerce product photo of digital alarm clock on bedside table, clean background, highly realistic, no text, no logo, slight angle"
gen docs/images/alarm_clock/003.jpg "realistic ecommerce product photo of digital alarm clock on bedside table, clean background, highly realistic, no text, no logo, close-up detail"

echo "images generated"
