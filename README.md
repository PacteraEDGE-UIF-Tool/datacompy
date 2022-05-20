# Log analysis
## Introduction
A simple program to compare the structured data and show the difference with GUI written in PyQt.

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Features

- Split file with pattern learning algorithm(prifix span).
- Compare the file pair and highlight the difference.
- Show the pattern learning result with a sequential graph.
- Automatically delete the file pairs with same content inside.
 
## Installation & Quick start

```bash
cd dependency analysis
pip3 install -r requirement.txt
cd datacompy #(if folder is not exist, clone the repo from our company's private repo)
python3 setup.py install
cd ..
python3 main.py
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
## Tech

This project reference to following repo or algorithms.

- [Prefix span] -https://github.com/chuanconggao/PrefixSpan-py
- [datacompy] - https://github.com/capitalone/datacompy
- [pandas] - https://pandas.pydata.org/
- [pyqt6] -https://pypi.org/project/PyQt6/



