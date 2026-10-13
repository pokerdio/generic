# Space prototype

On Linux Mint / Ubuntu:

```sh
sudo apt update
sudo apt install build-essential libraylib-dev pkg-config
make
./space
```

If `libraylib-dev` is not available from your configured repositories, install raylib from source (https://github.com/raysan5/raylib) and then run `make`.

Commands (press Enter):

- `AK-BM` select the rectangle containing sectors AK and BM
- `AK-BMAJ` same with different sector resolutions
- `A-D` select columns A through D
- `+BMDL` add planets in a sector to the current selection
- `&BMDL` intersect selection with a sector (if none selected, starts with that sector)
- `t>0.5&m<0.2` combine resource filters
- `z BMDL` zoom the map to a sector; `z` restores full map
- `d 1`, `d -1`, `d 10`, `d -10`, `d 1/3`, `d -2/9` position the table
- `d 1/2 t` sort by tritanium and center the median row
- `d -m -1` sort descending by molybdenum and show last row at bottom

No spaces inside filter expressions. Command-line selection affects red/white map dots and the table; zoom is independent.

Note: to guarantee unique names, even a final cell with exactly two planets gets suffixes 1 and 2.
