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
    orcid: 0000-0002-5080-6809
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
building platform that allows researchers to develop and manage surveys using a GUI or by writing 
Python code. When a survey is accessed by an end user, OpenQuestion renders it, according to design,
as an interactive web application for data acquisision.
^[OpenQuestion is built with the open source Anvil App Server, a runtime engine for 
writing full-stack web applications in Python [@anvil].Note that an Anvil account
is not required to use OpenQuestion.]

# Statement of need
OpenQuestion's GUI and general functionality will be familiar to researchers who have used 
commercial survey platforms. However, OpenQuestion is unique in comparison since 
much of the platform can be controlled via Python^[Those without Python knowledge can simply use OpenQuestion's GUI as a 
free alternative to other commonly used survey platforms.]. There are two main features that allow researchers
to leverage Python for survey development/management:

- Surveys designs are stored as a Python `dict`/JSON
- A Python interpreter can be connected to OpenQuestion's internal database

As a result, researchers familiar with Python could, for example, perform the following tasks with OpenQuestion:

- Batch create surveys
- Archive survey designs
- Perform CRUD tasks on the backend database (e.g., survey and/or user management)

In addition to using Python code to interact with OpenQuesion, the GUI also includes the following
researcher-friendly features that are often not available in commonly used commercial survey platforms:

- Markdown widgets can be used to quickly write rich text areas (as well as 
to embed images, GIFs, links, etc.)
- Query strings parameters can be added to URLs. This allows data that the end-user _did not_ 
indicate on the web form to be merged with a submission. This meta data can then be used for downstream 
data processing and/or analysis
- A labelled slider bar widget can be used to collect continuous quantitative data

Another notable Python-based survey platform is Docassemble [@docassemble]. In contrast
to OpenQuestion, Docassemble focuses on document generation, and in terms of development, web forms are 
created by writing YAML, Markdown, and Python. OpenQuestion on the other hand, is designed for surveys 
that save submissions to a database and survey development can be accomplished using the 
GUI or by writing Python code. Docassemble is a mature project with a thriving
community and should be considered by researchers looking to automate document generation via web-based forms.

# Acknowledgements
The authors would like to thank 
James Desjardins, 
Stefon van Noordt, 
Meredydd Luff,
Ian Davies,
Phil Colbert,
Grant Bryer,
Stephanie Spicer,
Trevor Dixon,
Lisa Collimore, 
Jennifer MacDonald,
Zoe Walters,
Whedon,
the Journal of Open Source Software, 
the Halton Catholic District School Board, 
and the Anvil community
for their support of this project.

# References