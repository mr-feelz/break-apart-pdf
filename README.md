# break-apart-pdf
Converts each page of a multi-page PDF into it's own PDF document. 

## Description
This is an easy to use Python script that converts each page of a multi-page PDF file into their own individual PDF files.

The script I uploaded is straightforward but you may need to make modifications to accomidate for your specific use.

## Usage
With my specific use, I included a segment of the script that checks the footer for a page number. This page number is then used to title each PDF file that is outputted. For example, a 5 page PDF file will return files named as "Page_1.pdf", "Page_2.pdf", "Page_3.pdf", etc. This is very useful if you are using this script on a specific segment of a multi-page PDF (ex. pages 25-45). 

## What to change
Lastly, you will need to specify your input PDF and output folder location. This is found at the bottom of the script:

```
pdf_path = "<INPUT PDF>.pdf"
output_folder = "<OUTPUT FOLDER>"
```

A very useful script, hope it helps.

