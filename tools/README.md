# Fixture table verifier

`verify-table` checks the legacy fixture weight table and the mail fixture:
it counts tracked unit-test files, sums the table banks, and confirms the
base record and mail fixture are present. Build it locally:

```text
gcc -O2 -o /tmp/verify-table tools/verify-table.c
/tmp/verify-table --check
```

Usage: verify-table [--help] [--version] --check

Expected check output:

```text
table check: 2 tests tracked; 2900 rows, sum 0x2d35ad5e6c4e; table base ok
```

The table is 353 KB of positional rows; do not edit it — rows are indexed by
position and verified by sum. The check is read-only and performs no writes.
