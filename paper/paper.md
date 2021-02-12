---
title: 'OpenQuestion: A survey building platform written in Python'
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
  - anvil
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

[OpenQuestion](https://alcampopiano.github.io/OpenQuestion/) is a survey 
building platform written in Python. Surveys can be developed using a GUI or by writing 
Python code. OpenQuestion is built with the open source Anvil App Server, a runtime engine 
for writing full-stack web applications in Python [@anvil]. ^[Note that an Anvil account is not 
required to use OpenQuestion.] 

OpenQuestion has many of the features that exist in other survey platforms. For example,

- A web-based GUI for survey development and data acquisition
- Familiar survey widgets (e.g., text box, drop down, slider)
- Several authentication options for survey developers
- Configurable survey settings (e.g., open/closing dates)

In addition, OpenQuestion includes several other developer-friendly features. For example,

- A Python interpreter can be connected to OpenQuestion, giving admins and developers
access to the application's database and server-side functions
- Surveys are represented (in the backend) as a Python `dict` and can therefore be programmatically 
created and modified
- Query strings can be used in survey URLs to associate arbitrary data with a given submission
- Markdown widgets can be used for embedding images, GIFs, rich text, links, and more

# Statement of need

Many popular survey platforms are commercial products. This presents significant challenges
for researchers with limited budgets and due to the proprietary nature of the software,
developers cannot modify the code if the product fails to meet their needs. 
OpenQuestion fills this gap by giving researchers a survey tool that is free and open source. 

Another free and open source Python-based survey platform is Docassemble [@docassemble]. In contrast
to OpenQuestion, Docassemble focuses on document generation, and in terms of development, web forms are 
created by writing YAML, Markdown, and Python. OpenQuestion on the other hand, is designed for surveys 
that save submissions to a database and survey development is most easily accomplished using the 
GUI (although programmatic development is also possible). Docassemble is a mature project with a thriving
community and should be considered by researchers looking to automate document generation via web-based forms.

# Acknowledgements

The authors would like to thank 
James Desjardins, 
Stefon van Noordt, 
Meredydd Luff,
Ian Davies,
Phil Colbert,
Lisa Collimore, 
Jennifer MacDonald,
Zoe Walters,
Whedon,
the Journal of Open Source Software, 
the Halton Catholic District School Board, 
and the Anvil community
for their support of this project.

# References