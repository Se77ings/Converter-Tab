# Guitar tab converter: Position to Note  

## General
The general idea is to place the guitar solo tab in a file named "file.txt":
Example:  
```
E|----------------------------------------------------|
B|--------8-------------8b10-b10r8--------------------|
G|----7h9---9~------7h9------------9~-----------------|
D|----------------------------------------------------|
A|----------------------------------------------------|
E|----------------------------------------------------|

E|------------------------------b12r10-8--------------|
B|-----8/10-8-8/11-13-13-b15r13----------10~----------|
G|-7h9------------------------------------------------|
D|----------------------------------------------------|
A|----------------------------------------------------|
E|----------------------------------------------------|
```
And the program will convert and print the formatted solo tab as follows:  
``` 
E|----------------------------------------------------|
B|--------G-------------G↑A-↑A↓G----------------------|
G|----D→E---E~------D→E------------E~-----------------|
D|----------------------------------------------------|
A|----------------------------------------------------|
E|----------------------------------------------------|

E|------------------------------↑E↓D-C----------------|
B|-----G/A-G-G/A#-C-C-↑D↓C---------------A-~----------|
G|-D→E------------------------------------------------|
D|----------------------------------------------------|
A|----------------------------------------------------|
E|----------------------------------------------------|
```

## Obs
PS: I changed the regular techniques like 'h' (hammer-on) to just an arrow, so it became like this:  
Original | Transformed
:---: | :---:
h | →  
p | ←  
b | ↑  
r | ↓  
