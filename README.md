# RTAC CSV Converter

Converts the outputs of a Google form response sheet with many lighting requests into many individual sheets of lighting requests. 

---
### How to use:
 * In Google Drive, open the form responses and select `File -> Download -> Comma-seperated value (csv)`. Place the file in the same folder as `ConverterApp.py`
 * Double click and run `ConverterApp.py`. Python 3 is recommended, but Python 2 should work.
 * Input the filename, **without** the `.csv` extension, in the first box.
 * Give names to the "preamble" of the responses sheet. This lets the app know what information to expect *before* it starts seeing cues. The default is `time, bcemail, Song, Contact Name, Email, Costume Color, Costume Texture, Music Length`. This means it expects to see those items of information as the first 8 columns of the sheet, **in that order**. Each name must be seperated by a comma.  
    * This default is for the 2020 Dance Group form. For the 2019 WOD form, a preamble description may look like 
    `time, bcemail, Group Name, Email, Costume Color, Costume Texture, Song, Music Length`
    * These names are used later and they must match **exactly** when used again (they are case sensitive!).
        * These names are not magic -- changing `Song` to `xchshwDGD` wouldn't matter, as long as you were consistent
 * Pick **one of the above pieces of information** to be the name of the output file. The default is `Song`.
 * Describe which preamble information of the above should be put in the header of each file. The default is `Song, Contact Name, Email, Costume Color, Costume Texture, Music Length`.
 This generates a header which looks something like
    Song | Somebody to Love
    ---|---
    Contact Name | Jane Doe
    Email | whatever@whatever.com
    Costume Color | Blue
    Costume Texture | Sequins
    Music Length | 6:04
    
but this can be easily customized by changing which pieces of info appear in what order.
 * Give a list of descriptive names to the information given for each cue, in the order it appears in the spreadsheet. Similar to preamble, these names can be anything, but the default of `Time, Fade, Feeling, Cyc, Happening` matches RTAC conventions for the past several years.
 * Specify the maximum number of cues that the program should read. `25` is the default.
 * Hit convert
 * This will generate a bunch of .csv files, one for each dance. Re-upload these to Google Drive, and when you open them in sheets they will be converted back into Google Sheets files.
