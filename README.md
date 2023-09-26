# Random ID generator

This is a simple random ID generator. It generates random IDs given a specificed pattern.

## Usage

```bash
usage: make_random_id.py [-h] [-i INPUT | -n NUMBER] [-x EXCLUDE_LIST] -o
                         OUTPUT -p PATTERN [--no_head]

Make random id

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file. One random id will be generated per line
  -n NUMBER, --number NUMBER
                        Number of random id to create
  -x EXCLUDE_LIST, --exclude_list EXCLUDE_LIST
                        A file containing a list of IDs to exclude, i.e.
                        previous IDs to avoid duplication
  -o OUTPUT, --output OUTPUT
                        Output file
  -p PATTERN, --pattern PATTERN
                        Pattern, like "AA_@3xLU@-@2xD@"
  --no_head             Input file has no header and no header in output
```

## Pattern

The pattern is a string that can contain any combination of characters, but not spaces. Random elements within the string are defined between `@` characters.

Random elements are composed by:

1. a number defining the number of random char to generate
2. "x" char
3. a tag defining the set of chars to use

For example, `@3xLUP@` will generate 3 random uppercase letters

### Tags

The following tags are allowed:

| Tag | Description |
| --- | ----------- |
| LUP | Uppercase letters |
| LLOW | Lowercase letters |
| L | Letters (mixed upper and lowercase) |
| LD | Uppercase letters + digits |

### Examples

| Pattern | Example |
| ------- | ------- |
| `@3xLUP@-@2xD@` | `ABC-12` |
| `@3xLLOW@-@2xD@` | `abc-12` |
| `FIX_@2xLUP@@3xD@` | `FIX_AB123` |
| `FIX-@2xD@-@3xLUP@` | `FIX-12-DEF` |

## Exclude list

You can specify a list of IDs to exclude from the random generation usin `--exclude_list`. This accepts a text file with one ID per line.

This is useful if you want to generate new IDs for an existing project, but you want to avoid generating IDs that already exist.
