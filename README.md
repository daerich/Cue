# CUE - a C-pre-pre-processor
#### Cue is a C pre-pre-processor adding some minor functionality from modern Languages (like globbed import - inspired from Rust/Python) to C.

Currently it features:
- Globbed include
- String extended include
### Usage
```
LIBPATH=/path/to/system/include g.py [FILE..] > preprocessed_files.c
```
### Bugs
- Currently only writes to stdout
