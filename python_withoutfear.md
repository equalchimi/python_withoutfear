# miniconda

*for switching between versions of python*

## AnacondaPrompt

*terminal to get into python, install other versions, etc.*
* cannot run things

```
tip: search "Conda Cheat Sheet"

link: https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf
```
* getting started in anaconda:

 *to change versions* 

  ```
  activate VERSIONNAME (say, py362)  
  ```
  
 *start up python!*
  ```
  python  
  ```
 *should see this when you're in python*
  ```
  >>>  
  ```
 *to exit python, remains in version*
  ```
  ^Z  
  ```
  
 *to exit that version and return to base*
  ```
  deactivate  
  ```
 
      
   * to check what version base is, type 
      ```
      conda info
      ```
     while in anaconda, not python


        * tip: right click open in vs code in **folder** or **directory** so can create new files etc.


## Change environment (py version) in vs code

```
ctrl shift p
```
or, go to View >> Command Palette

search **Python Select Interpreter

click it, and select desired version 


## Import sys (or whatever package)

*in order to use a package in vs code, must type*
```
import PACKAGE
```
* note, can place import commands in middle of code, but only code after the command may use that package. that's why it's better/customary to place them all at the beginning (yes, one file can use many imports)


# General notes:

* packages are main in python (can do different things with each package)

* Inheritance:
```
>>>base (parent)
  >>>derived (child)
```
*each 'category' is called a **class***
```
ex. 
>>>shape
  >>>triangle, square, rectangle, etc.
        ^         ^       ^
        these are classes. can be more specific
```
* consistently use 4 spaces or a tab

* in vs code: ctrl , *open settings*
         
    
    
 # miniforge (same function as miniconda)
 
 *google one word 'miniforge'*
 *click on the github link*
 
 download **mambaforge for Windows x86_64**
 
 *select the rec. setting*
 
 ## creating Conda environment
 
 *so you can manage many versions of python*
 
 ```
 conda search python
 conda create --name #customname(usually py##) python=#version.num
 ```
 
 ## using Conda in VS Code
 
 go to settings: search 'Terminal Default'
 
 go to the Windows setting: change to 'Command prompt'

 now you can type 
 
 ```
 python #filename(like ch2.py)
 ```
 in terminal window (in vs code)
 
 after that, to run, just up arrow and enter
 
 
 ## using python terminal in windows terminal
 
 go to location of py files in windows file explorer
 on location bar, type wt (opens windows terminal)
 press dropdown, go to settings, go to gear (open json file)
 scroll down to cmd.exe (ctrl f)
 paste:
 ```
 {
                "commandline": "cmd.exe /K %USERPROFILE%\\local\\mambaforge\\Scripts\\activate.bat %USERPROFILE%\\local\\mambaforge",
                "fontSize": 10,
                "guid": "{28b5f9c0-6c5b-4e6c-b9d8-ea4e53421265}",
                "hidden": false,
                "name": "Mamba Prompt",
                "startingDirectory": "."
            },
```
after the cmd chunk

*from script above, can see that can change mamba's fonst size when using it in wt*
to change color of mamba in wt, go to:

settings

appearance

change color scheme/system colors as wanted 

go to:

mamba (on the left bar)

appearance

change to the color scheme you created/changed from before

save!

## migrating notes from github to vs code

go to the desired location in file explorer

open vs code there

create new file, copy paste name/rename, make sure ends with .md

in your gist, go to raw

ctrl a and ctrl v!

# backing up to git

go to wt default command prompt
type 
```
git init .
git add -i
```
add as needed

```
git s
```
*s for status (for us only)

```
git remote add origin https://equalchimi@github.com/equalchimi/python_withoutfear.git
```
*connecting to github repository, allows to upload to github* 

*adding username before github bypasses getting asked everytime*
  
```
git remote -v show
```
*shows what remote you have/what you changed* 




