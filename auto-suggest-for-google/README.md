# Auto-Suggest for Google

This script can be run to output the google suggestions for a partcular keyword.<br>
This can also be used to provide similarly searched words to build a database for NLP.<br>

To run the script:

> python3 auto-suggest-for-google.py [file path where keywords are stored]

Example:

```python
python3 auto-suggest-for-google.py kws-for-auto-suggest.txt

# Output file: auto_suggest_result.txt

hello:
  2         hello
  3         hello google
  4         hello hello
  5         hello guru prema kosame
  6         hello app
  7         hello movie
  8         hello brother
  9         hello how are you
 10         hello google kaise ho
 11         hello sir
 12 
 13 
 14 boston:
 15         boston
 16         boston time
 17         boston consulting group
 18         boston weather
 19         boston university
 20         boston marathon
 21         boston celtics
 22         boston scientific
 23         boston temperature
 24         boston legal
 25 

...

```


