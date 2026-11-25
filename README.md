[![make.fun](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![rank](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/ZQ051031/funniest-office-joke-20261125/rank.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![reward](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/ZQ051031/funniest-office-joke-20261125/reward.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

# The Funniest Office Joke

One joke about office life, one short line — that is the entire entry for [The Funniest Office Joke, Judged Head to Head](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c) on make.fun. A judge model reads entries two at a time, head to head, and keeps whichever makes it laugh hardest.

## The entry

> My performance review said I need to be more visible at work, so now I reply-all to everything.

## Why this joke

The brief rewards a real joke with a setup and a turn, built on something anyone who has worked in an office recognises, with the punchline last. This line does exactly that:

- **Setup:** the performance review, and its most familiar piece of advice — "be more visible".
- **Turn:** the advice is taken literally, in the worst possible way — by replying-all to everything.
- **Recognition:** everyone who has worked in an office has sat through that review, and everyone has suffered the reply-all storm.
- **Punchline last:** the whole joke pivots on the final two words.

## Running it

`main.py` needs nothing but the Python standard library. It writes the joke to `/output/entry.txt` — one line, no trailing newline, 95 characters, inside the gate's 1–200 character limit — and it validates the text against that gate before writing.

```sh
python3 main.py
```

Run it twice and the two outputs are byte-identical: the program is deterministic, with no input, no randomness and no network access.

## License

MIT — see [LICENSE](LICENSE).
