# Gym tasks

Tasks to point an agent at, roughly in order of difficulty. Each one is
designed to need several tool calls and more than one file.

## 1. Fix the failing tests (the main one)

> Two tests are failing. Find out why and fix the source, not the tests.

Exercises: shell_exec (pytest), code_search (find `qualifies_for_bulk` -- two
hits, one is the frozen legacy module), fs_read with line ranges, fs_write,
re-running tests to verify. The trap: "fixing" `legacy_pricing.py` also makes
nothing better and violates docs/PRICING.md.

## 2. Catalogue question

> What is the unit price of SKU-1337, and how many products are in the
> `bearings` category?

Exercises: code_search on a 640-line file that a whole-file read would choke
on. Punishes reading catalog.py end to end.

## 3. Small feature

> Add a `line_count()` method to Order returning the number of lines, with a
> test for it.

Exercises: fs_read a slice of orders.py, fs_write, test authoring, pytest.

## 4. Cross-file consistency

> The free shipping threshold should be 400, not 500. Update it everywhere,
> including any test or doc that mentions the old value.

Exercises: search across code, tests and docs; multiple edits; verify.
