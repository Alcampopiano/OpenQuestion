# FAQ
Suggestions for FAQs are welcome. Please submit these to OpenQuestion's
issues [page on GitHub](https://github.com/Alcampopiano/OpenQuestion).

## How do I download submissions for a survey?
In the [survey dashboard](survey_dev.md#survey-dashboard) click
the :material-database: icon.

## How do I get a shareable URL for survey?
In the [survey dashboard](survey_dev.md#survey-dashboard) click
the :material-link: icon.

## Is it possible to have a specific URL for each end user?
This sounds like a good job for
[query strings](advanced.md#adding-data-to-submissions-using-query-strings).
Just design your URLs with the desired parameters and OpenQuestion
will merge and/or add any additional data to each submission.

## Are matrix-type widgets available?
Not yet! But requests are welcome on OpenQuestion's issues page on GitHub.
For now, one would have to flatten out items into multiple
widgets ☹️.

## How do I add an image to my markdown widget?
markdown widgets support web-hosted images. This means
that any publically hosted image address should work with the usual
Markdown syntax. For example,

```markdown
![img](https://i.imgur.com/kZ9piPH.gif)
```

leads to this (from Imgur):

![img](https://i.imgur.com/kZ9piPH.gif)

## Can I add a header/footer to my survey?
Yes, well, sort of. One way to accomplish this would be to add the desired image
to your survey using a [markdown widget](widgets.md#markdown). Note that
currently OpenQuestion only supports a single page survey.

## Can I split my survey into separate pages?
Currently OpenQuestion only supports a single page survey. Section widgets
are used to visually delimit groupings of widgets but they are still presented
on the same page. This feature will be likely be implemented in a future release.

## Can I do any kind of data analysis and/or visualization in OpenQuestion
Not at the moment and likely it will stay that way. Originally, OpenQuestion included a 
so-called reporting module that allowed developers to 
add [VegaLite](https://vega.github.io/vega-lite/) specs 
and markdown widgets to a notebook-like web page to demonstrate their
findings. The reporting module still exists 
but is has been turned off to reduce the scope of this project. 
If fast and powerful metrics and visualizations are needed, there are many existing 
tools that do this far better than OpenQuestion ever could 😃.
For example, please see [Altair](https://altair-viz.github.io/), 
[Jupyter](https://jupyterlab.readthedocs.io/en/stable/), and [Deepnote](https://deepnote.com/).
