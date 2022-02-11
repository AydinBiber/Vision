# IAM Strikethough Database

This database is based on the IAM database. In order to not infringe on the copyright of the original database, this repository does not contain the modified images but only the diffs, which have to be merged with the original images.

**Please note that the IAM database may only be used for non-commercial research purposes. This is therefore also the case for this derivative work.**


In order to obtain the actual strikethrough database, please follow the steps below:
1. download the original IAM database, specifically the ```words``` directory
2. modify [code/prepare_iam_strikethrough.py](code/prepare_iam_strikethrough.py) with the following information:
  1. the path to the aforementioned ```words``` directory (variable ```wordsDirectory```)
  2. the base directory containing the unzipped ```train```, ```validation``` and ```test``` directories from this repository (variable ```dataDirectory```)
  3. the desired output location (variable ```outputDirectory```)
3. install the following Python dependencies (versions used by the authors given in parentheses, though many other versions should work just as well):
    - ```numpy``` (1.19.5)
    - ```scikit-image``` (0.17.2)


### Code for the creation of the original strikethrough images
If you are looking to reproduce this database from scratch, please consult the code in [code/creation](code/creation) and its separate README.

Please **note** that the code in the aforementioned directory is 1:1 the exact code that was used. If you are interested in applying strikethrough to your own dataset, please consider using the following package instead, which provides better documentation and may be developed further in the future: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4767063.svg)](https://doi.org/10.5281/zenodo.4767063)


### Citation

#### Original IAM database:
```
@article{marti2002iam,
  title={The IAM-database: an English sentence database for offline handwriting recognition},
  author={Marti, U-V and Bunke, Horst},
  journal={International Journal on Document Analysis and Recognition},
  volume={5},
  number={1},
  pages={39--46},
  year={2002},
  publisher={Springer}
}
```

#### Strikethrough Removal Paper:
```
@INPROCEEDINGS{strikethrough,
  author={Heil, Raphaela and Vats, Ekta and Hast, Anders},
  booktitle={2021 International Conference on Document Analysis and Recognition (ICDAR)},
  title={{Strikethrough Removal from Handwritten Words Using CycleGANs}},
  year={2021},
  pubstate={to appear}}
```
