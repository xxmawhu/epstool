# epstool

## function

A tool cut the black margin of eps figure
## How

Base on `gs`
* first, get the bounds of the eps figure using the following command
```bash
gs -dNOPAUSE -dBATCH -q -sDEVICE=bbox fileName.eps 
```
The output is, i.e 
```
%%BoundingBox: 0 1 258 167
%%HiResBoundingBox: 0.594000 1.224000 257.140820 166.921800 
```
* Then, replace the BoundingBox with the output value, usually lying at the first
3 lines of the eps figure.

## Usage
* set up the environment
```bash
source setup.sh
```
* Cut Cut Cut
```bash
epstool fileName.eps
```
