py_merge_files
---

Merge all files in input path.

```
usage: merge_files [-h] [-o OUTPUT] [-e EXTENSIONS] [-b MB] input

positional arguments:
  input                 input file name

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output file name
  -e EXTENSIONS, --extensions EXTENSIONS
                        allowed file extensions (comma separated)
  -b MB, --buffer-length MB
                        default to 10 megabytes
```