# mlb-normalize-player-ids

A quick and dirty one-stop CLI for taming disparate and wild
baseball player ID registers.

Currently supports CSV registers from:

- [Chadwick Register](http://chadwick-bureau.com/the-register/)
- [Smart Fantasy Baseball](http://www.smartfantasybaseball.com/tools/)
- [Crunchtime Baseball](http://crunchtimebaseball.com/baseball_map.html)

## Installation

Install this script via `pip`:

```shell
$ pip install -e git+git@github.com:mattdennewitz/baseball-normalize-player-ids.git#egg=baseball-normalize-player-ids
```

or clone this repo and work with it directly.

## Usage

Once installed, use `bid_normalize_register.py` to normalize schemas.
`bid_normalize_register` understands three conversion types:

- `chadwick`, for the Chadwick Register
- `sfbb`, for Smart Fantasy Baseball's Player ID map
- `crunchtime`, for Crunchtime's MLB Player Names and IDs map

Example:

```shell
$ bid_normalize_register.py -s chadwick -i /path/to/chadwick-register.csv /path/to/output.csv
```
