---
title: 'OpenQuestion: A Web-Based Survey Platform written in Python'
tags:
  - python
  - survey
  - forms
  - formstack
  - microsoft
  - google
  - anvil
  - qualtrics
  - cognito
  - docassemble
authors:
  - name: Allan Campopiano
    orcid: 0000-0002-3280-4447
    affiliation: 1
  - name: Stu Cork
    orcid: xxxx-xxxx-xxxx-xxxx
    affiliation: 2
    
affiliations:
  - name: Halton Catholic District School Board
    index: 1
  - name: Anvil
    index: 2
date: 20 Jan 2021
bibliography: paper.bib
---

# Summary

[OpenQuestion](https://alcampopiano.github.io/OpenQuestion/) is a web-based survey 
building platform written in Python. Surveys can be developed using a GUI or by writing 
Python code. OpenQuestion is built upon the open source Anvil App Server, a runtime engine, 
for writting full-stack web applications in Python [@anvil]. ^[Note that an Anvil account is not 
required to use OpenQuestion.] 

OpenQuestion has many of the features that exist in other survey platforms. For example,

- A web-based GUI for survey development and data acquisition
- Familiar survey widgets (e.g., text box, drop down, slider)
- Several authentication options for survey developers
- Configurable survey settings (e.g., open/closing dates)

In addition, OpenQuestion includes a number of other developer-friendly features. For example,

- A Python interpreter can be connected to OpenQuestion, giving admins and developers
access to the application's database
- Surveys are represented (in the backend) as a Python `dict` and can therefore be programatically 
created and modified
- Query strings can be used in survey URLs to associate arbitrary data with a given submission
- Markdown widgets can be used for embedding images, GIFs, rich text, links, and more

Another notable Python library that can be used for web-based data collection is Docassemble [@docassemble]. Web forms 
in Docassemble (so-called guided interviews), are developed by writing YAML, Markdown, and Python. 
In contrast to OpenQuestion, Docassemble is focused on document generation based on the answers provided in 
the guided interview. OpenQuestion on the other hand, is designed for surveys that save submissions 
to a backend table. Further, surveys in OpenQuestion can be designed using a GUI (as well as by using Python) 
and therefore developers with limited technical expertise may have a lower barrier to entry. 

# Acknowledgements

The authors would like to thank 
James Desjardins, 
Stefon van Noordt, 
Meredydd Luff,
Ian Davies,
Lisa Collimore, 
Jennifer MacDonald,
Zoe Walters,
Whedon,
the Journal of Open Source Software, 
the Halton Catholic District School Board, 
and the Anvil community
for their support of this project.

# References