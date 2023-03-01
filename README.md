# Bulk number creator

This tool gonna be used in case you have a portion of a number (currently worked if you have last numbers) You can select ISP and then Enter the phone number last digits that you have, after that it will create an excel file with every possible combination numbers with given last digits.



## Install and Requirements

python 3.6+

```
pip install -r requirements.txt
```


## Usage

Enter ISP name:
```
please enter ISPs (MTN, MCI, RTL) or enter (exit) to close: 
```

Enter the last digits (No matter how many digits you have):
```
please enter the number that you have:
```

The output you will give would be a .XSLX file in the source code folder.

## Validation

The only validation that we have currently is a number possibility checker using some python library.

## Known Issues and What I'm working on it  

* The number of generated phone numbers is so high, it is near to impossible to save __And__ check all of them in social medias and messengers. 

* The Validation method is not useful, I've found a way to validate them all using official ISP websites but the current approach that I'm trying has low speed and not much reliability. 

* Output is limited to Excel (XSLX) format, I'm gonna add more formats ASAP.

* Code structure is not quite good, but its and MVP, Proof of concept, and early-stage script.
