# CLI4BigFiles
## Welcome to my own CLI, that can create random files, modify them, and increase them.

The task was to write a console utility for generating files with arbitrary content.

### The interface of this CLI:
```
file_generator --file-name=out.tst --size=120G
```
Generating an out.tst file with random content of 120 gigabytes in size (alternatively, modifiers M can be specified - megabytes, K - kilobytes, number without a modifier - bytes).
```
file_generator --file-name=out.tst --modify --percent=5
```
Change the out.tst file by 5% (random parts of the file are replaced by random blocks by 5% of the file size).
```
file_generator --file-name=out.tst --increase --perсent=5
```
5% increase in out.tst file (random data is written to the end of the file).
### Installing
For installing this utility, you need to start setup.py in the main folder of the repository.
```
python setup.py develop
```
If everything passes correctly, the script is ready to use. Now you can use it in Anaconda Prompt by typing:
```
file_generator --help
```
## Built With

* [Click](https://click.palletsprojects.com/en/7.x/) - The library for crating CLI's

### Please, send me your feedback. 
