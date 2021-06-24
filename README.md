# CUE - a C-pre-pre-processor
#### Cue is a C pre-pre-processor adding some minor functionality from modern Languages (like globbed import - inspired from Rust/Python) to C.

Currently it features:
- Globbed include
- String extended include
### Usage
```
LIBPATH=/path/to/system/include q.py [FILE..] > preprocessed_files.c
```
### Demonstration:
Suppose you have the following trivial include.

main.c:
```
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
```
That's an awful lot of writing...
However... there is a solution

Just let Cue take care of that:

Rewrite main.c:
```
#include <std{io,lib}.h>
#include <sys/{stat,types.h}>
```
after
```
LIBPATH=/usr/include/ q.py main.c
                    ^
                    |------ slash is significant
```
main.c will become:
```
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
```
again.

### Bugs
- Currently only writes to stdout



_I became almost insane fiddling with string santitation._
