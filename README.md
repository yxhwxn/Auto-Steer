# Auto-Steer

## License

This prototype implementation is licensed under the 'MIT license' (see LICENSE).

## Requirements

### Packages

- sqlite3
    - Statistics extension (we provide a download script: `sqlean-extensions/download.sh`)
- python3 (at least version 3.10)

### Python3 requirements

- Install python requirements using the file `pip3 install -r requirements.txt`

## Run Auto-Steer

### Database Systems

#### Auto-Steer-G already supports five open-source database systems:

- MySQL
    - We tested AutoSteer with MySQL 8

#### DBMS Configuration

Depending on your custom installation and DBMS setup, add the required information to the `configs/<dbms>.cfg`-file.

### Executing Auto-Steer's Training Mode

Auto-Steer's training mode execution consists of two steps:

1. (A) Approximate the query span, and (B) run the dynamic programming-based hint-set exploration
   ```commandline
   main.py --training --database {postgres|presto|mysql|duckdb|spark} --benchmark {path-to-sql-queries}
   ```
2. By now, Auto-Steer persisted all generated training data (e.g. query plans and execution statistics) in a
   sqlite-database that can be found under `results/<database>.sqlite`.
3. For PrestoDB query plans, we implemented the preprocessing of query plans for tree convolutional neural networks.
   ```commandline
   main.py --inference --database presto --benchmark {path-to-sql-queries}
   ```
4. The inference results can be found in the directory `evaluation`.

## Code Formatting

- All python files will be checked using `pylint` before they can be comitted. The code style is primarily based on
  the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
  However, it allows longer lines (160 characters).
- Please, install and run pylint (there is also a git pre-commit hook) before committing

## Cite
If you use AutoSteer in your work, please cite us:
```
@article{autosteer2023,
    author       = {Anneser, Christoph and Tatbul, Nesime and Cohen, David and Xu, Zhenggang and Pandian, Prithviraj and Laptev, Nikolay and Marcus, Ryan},
    date         = {2023},
    journaltitle = {PVLDB},
    number       = {12},
    pages        = {3515--3527},
    title        = {AutoSteer: Learned Query Optimization for Any SQL Database},
    volume       = {16},
}
```
