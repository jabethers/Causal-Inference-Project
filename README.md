# Analyzing Positional Spending in DraftKings Sunday Millionaire Lineups


## Context

Daily Fantasy Sports (DFS) has grown in popularity, with platforms like
DraftKings hosting contests that attract hundreds of thousands of
participants weekly. One of the most prominent competitions, the Sunday
Millionaire, offers a grand prize of 1 million dollar for creating the
team that scores the most points under strict salary cap constraints.
Players must allocate a fixed budget (e.g., \$50,000) across a roster of
NFL athletes, carefully balancing star players with high salaries and
lower-cost value options.

Given the competitive nature and entry fees of these contests,
understanding the patterns behind winning lineups can provide actionable
insights for DFS players. Specifically, analyzing how winners allocate
their budgets across positions (e.g., Quarterback (QB), Running Back
(RB), Wide Receiver (WR), Tight End (TE), Defense/Special Teams (DST))
can reveal strategic approaches that increase the likelihood of success.

This project aims to investigate the relationship between positional
spending and the likelihood of winning the Sunday Millionaire contest.
By identifying spending patterns, such as positions where winners tend
to “spend up” or “punt,” we hope to provide a data-driven narrative
about optimal lineup construction strategies.

## Outcome

The primary outcome of this study is to identify and describe positional
spending patterns in winning DraftKings Sunday Millionaire lineups.
Specifically, we aim to:

Determine whether winners consistently allocate higher salaries to
specific positions.

Explore the relationship between spending patterns and total fantasy
points scored.

Offer actionable insights on optimal lineup construction strategies for
DFS players.

## Variables of Interest

## Dependent Variable:

Total Fantasy Points Scored: The total points accumulated by a lineup,
which determines success in the contest. This is the key metric for
evaluating lineup performance.

## Independent Variables:

Positional Spending: The salary allocated to each position in the
lineup, which must include:

Quarterback (QB)

Running Back 1 (RB1) and Running Back 2 (RB2)

Wide Receiver 1 (WR1), Wide Receiver 2 (WR2), and Wide Receiver 3 (WR3)

Tight End (TE)

Flex (RB/WR/TE)

Defense/Special Teams (DST)

## Explanatory Variables:

To control for factors that might influence both positional spending and
lineup success, we will include the five following variables:

1.  Player Ownership Percentage:

The proportion of lineups in the contest that included a given player.
Highly owned players are often considered “chalk,” while low-owned
players are “contrarian” picks.

2.  Player Matchup Quality:

Metrics like opposing defense rankings, implied team totals, and game
pace (plays per game) to account for the context of individual player
performance.

3.  Slate Context:

Characteristics of the week’s slate, such as the total number of games,
the availability of high-salary star players, and the diversity of
viable value options.

4.  Contest Size:

The number of participants in the Sunday Millionaire contest, which may
affect optimal lineup construction due to differences in variance and
risk tolerance.

5.  Salary Efficiency:

The points per dollar (PPD) of each player in the lineup, serving as a
measure of salary utilization efficiency.

## My Narrative

The “story” of this project revolves around uncovering the strategy
behind winning lineups in DraftKings Sunday Millionaire. By examining
historical data from Sunday Millionaire contests, we aim to identify
consistent patterns in how winners allocate their salary budgets across
positions. Do winners prioritize spending on star quarterbacks, or do
they find more success by investing heavily in running backs and wide
receivers? Is it more common to “punt” at the tight end or defense
positions, relying on low-cost options to free up budget for
high-ceiling players?

This narrative will evolve into a statistical model that explores these
questions. Its goal is to shed light on the causal relationships between
positional spending and lineup success. The model’s ultimate goal is to
provide a framework for understanding optimal DFS strategy, offering
practical advice to participants seeking to improve their chances in
future contests and increase overall fun to be had in these contests.

## Project Organization

- `/code` Scripts with prefixes (e.g., `01_import-data.py`,
  `02_clean-data.py`) and functions in `/code/src`.
- `/data` Simulated and real data, the latter not pushed.
- `/figures` PNG images and plots.
- `/output` Output from model runs, not pushed.
- `/presentations` Presentation slides.
- `/private` A catch-all folder for miscellaneous files, not pushed.
- `/writing` Reports, posts, and case studies.
- `/.venv` Hidden project library, not pushed.
- `.gitignore` Hidden Git instructions file.
- `.python-version` Hidden Python version for the reproducible
  environment.
- `requirements.txt` Information on the reproducible environment.

## Reproducible Environment

After cloning this repository, go to the project’s terminal in Positron
and run `python -m venv .venv` to create the `/.venv` project library,
followed by `pip install -r requirements.txt` to install the specified
library versions.

Whenever you install new libraries or decide to update the versions of
libraries you use, run `pip freeze > requirements.txt` to update
`requirements.txt`.

For more details on using GitHub, Quarto, etc. see [ASC
Training](https://github.com/marcdotson/asc-training).
