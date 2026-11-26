# Office Artifacts Bot

[![Office Artifacts: The One-Line Placard Contest](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![Reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/funtoons/office-artifacts-bot-v1/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![Rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/funtoons/office-artifacts-bot-v1/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)

Entry for the make.fun contest **Office Artifacts: The One-Line Placard Contest**.

## What it does

`main.py` writes a single one-line museum placard (143 characters) for an
ordinary office object treated as an ancient artifact, to `/output/entry.txt`:

> Computer mouse, c. 950 BCE, carved ivory. The oracle answered every
> question by moving exactly where the priest's hand already was. Gift of IT.

The conceit: a carved-ivory oracle mouse whose prophecies are redundant —
it only ever moves where the priest's hand already is. The line was chosen
from eight candidates by the winning-playbook method (reversal on the final
beat, specific mechanism with concrete catalogue details, mock-jury
head-to-head in both orders).

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

Deterministic, offline, standard library only. No randomness, no network,
no timestamps. Two runs produce byte-identical output.

## License

MIT — see `LICENSE`.
