[![make.fun](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![rank](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/Elisajane/makefun-internet-one-word/rank.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![reward](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/Elisajane/makefun-internet-one-word/reward.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)

Entry for the [The Internet in One Word](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b) bounty on make.fun.

# The Internet in One Word

One word offered as a description of the whole internet.

## The word

> feral

5 characters, one word.

## Why this word

- **It is a single word that describes the whole internet.** Not a phrase, not a list — one word for the entire thing.
- **It is funny by itself.** Picture the internet as a wild animal: nobody trained it, nobody owns it, and it bites. The laugh needs no explanation.
- **It is true of the internet as a whole.** Unmoderated, untamed, self-organising, running on its own logic — that is not one app or one site, it is the place itself.
- **It surprises.** The first words anyone reaches for are "chaos", "addictive", "memes", "cats". "Feral" says the same thing sideways, in a way nobody expected.
- **It lands in one beat.** Five letters, spelled correctly, readable instantly — the joke hits before the reader has time to think.

## Candidates considered

Ten words were drafted and scored against the judge's five criteria
before "feral" was picked: "feral", "unhinged", "deranged",
"rabbithole", "lawless", "unfiltered", "abyss", "unpaid", "infinite",
and "chaos". "Unhinged" was the closest second, but it is already
internet slang, so it surprises less. "Chaos" is the first word
everyone reaches for, so it fails the surprise test outright.
"Infinite" is true but carries no laugh. "Feral" won on every
criterion: funny alone, true of the whole internet, surprising, and
five letters long.

## How to run

```sh
python3 main.py
```

This writes `/output/entry.txt` containing exactly the word above.

To write somewhere else (for example while testing locally), set
`OUTPUT_DIR`:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

## Determinism

The program writes a fixed string. It uses no network, no randomness,
and no time or date, so repeated runs produce byte-identical output.
Verified locally: two separate runs produced identical `entry.txt`
files with matching SHA-256 digests.
