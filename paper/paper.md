---
title: 'OpenQuestion: A survey building platform written in Python'
tags:
  - python
  - survey
  - forms
  - formstack
  - microsoft
  - limesurvey
  - redcap
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
building and reporting platform for web-based data collection. Surveys 
can be developed using a GUI or programatically by writing Python code. To report on
survey results, OpenQuestion provides a Jupyter-like environment [@Kluyver:2016aa] 
for data visualization and document creation.^[OpenQuestion is built with the open 
source Anvil App Server, a runtime engine for writing full-stack web applications 
in Python [@anvil].Note that an Anvil account is not required to use OpenQuestion.]

# Statement of need
OpenQuestion's GUI and general functionality will be familiar to researchers who have used 
commercial survey platforms. However, OpenQuestion is unique in comparison since 
survey and report development can be controlled by Python^[Those without Python 
knowledge can simply use OpenQuestion's GUI as a
free alternative to other commonly used survey platforms.] and JSON.
The following section describes a few of the reasons why OpenQuestion can be useful for
data acquisition, analysis, and reporting.

## Surveys and report designs are stored as a Python `dict`/JSON
Since the format of both surveys and report designs are JSON, researchers can easily share,
archive, reformat, and "batch" create surveys and reports. For example, suppose a school board
uses OpenQuestion to create a form for a student census. If another school board would like to
use the same overall census design, they would simply need to request a copy of the underlying JSON
representation of the survey. Once the JSON is uploaded to OpenQuestion,
their web form would be fully operational, obviating the need for manual development using the GUI. 

## Analysis of survey data
OpenQuestion includes a reporting module that functions like a Jupyter-like environment in the sense that
rich text and interactive visualizations can be arranged on a page to form a narrative based on the survey data.
Specifically, OpenQuestion uses markdown widgets for rich text and chart widgets that use vega-lite
[@vegalite], a high-level, interactive visualization library. While reports are natively "connected" to their
associated survey's dataset, OpenQuestion also allows additional datasets to be loaded into any report. This
means that, unlike many other survey platforms, charting can occur across different 
data sets in the same report/environment.

### Automatic chart generation and templating
OpenQuestion's reporting module is able to automatically generate interactive charts 
(as well as their related vega-lite JSON representations). Automatic chart generation 
works in the following way:

- A user selects one or more columns in their dataset using a GUI

- OpenQuestion attempts to match those 
columns to one or more templates that are stored internally. 
Templates are simply vega-lite JSON specifications that have 
placeholders for a certain number of fields with given data 
types

- If one or more compatible templates are found, they are populated with the appropriate data,
and displayed in the report

In addition, once a user has a chart design that they would like to generally reuse 
(possibly with a different dataset), they can save the chart as a template. The next time
automatic chart generation is used, this new template will be considered in the matching process.
Automatic chart generation and templating is depicted in the figure below:

![OpenQuestion's automatic chart creation and templating process](https://alcampopiano.github.io/OpenQuestion/img/auto_chart_fig.png)

## Interactive "code-free" HTML reports
OpenQuestion allows reports (which include interactive charts and rich text) to be exported
to HTML files. All code blocks are removed and the interactivity of the charts is maintained. This is useful
for preparing manuscripts that are to be shared with either a non-technical audience 
(since there are no code blocks), or with colleagues and/or supervisors who would prefer to only see
the narrative aspect of the report (i.e., charts and text).

# Comparison to other survey development platforms
OpenQuestion's graphical interfaces (for developing and managing surveys), installation,
and documentation are intended to create a low barrier to entry for researchers. This 
contrasts with platforms such as REDcap [@harris2009research] (not open source; written in PHP) and 
LimeSurvey [@lime] (open source; mostly written in PHP) which have a potentially higher 
barrier to entry for many researchers (due to licensing, installation, complex interfaces, etc.). 
Although, it is also true that these platforms
are more mature and therefore have more features.^[Note that neither REDcap nor 
LimeSurvey are written in Python. This is only to say that 
perhaps there is an argument for OpenQuestion being an easier platform to contribute code to
for many researchers.]

One notable Python-based survey platform is Docassemble [@docassemble]. In contrast
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
Shaun Taylor-Morgan
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