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

## How do I add an image/GIF to my markdown widget?
[markdown widgets](widgets.md#markdown) support web-hosted images. This means
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

## Can I perform data analysis and/or visualization in OpenQuestion?
Not at the moment and likely it will stay that way. Originally, OpenQuestion included a 
so-called reporting module that allowed developers to 
add [VegaLite](https://vega.github.io/vega-lite/) specs 
and markdown widgets to a notebook-like web page to demonstrate their
findings. The reporting module still exists 
but it has been turned off to reduce the scope of this project. 
If fast and powerful metrics and visualizations are needed, there are many existing 
tools that do this far better than OpenQuestion ever could 😃.
For example, please see [Altair](https://altair-viz.github.io/), 
[Jupyter](https://jupyterlab.readthedocs.io/en/stable/), and [Deepnote](https://deepnote.com/).

## Can I change the color of a survey?
Yes, please see [this part](settings.md#survey-color) of the settings page.

## Can I change the default authentication services (for admins)?
Survey developers must authenticate into OpenQuestion. Various authentication options are available 
and can be configured by editing the file "anvil.yaml" located at the top level of OpenQuestion.
Inside that file you will see the following section:

```yaml
client_config: {allow_signup: false, enable_automatically: false, use_email: true,
  confirm_email: false, use_microsoft: true, require_secure_passwords: true}
```

By default, OpenQuestion includes the entries `use_email: true` and `use_microsoft: true` (described below).
You can remove these entries or set them to `false` if you would like to remove them as 
authentication options in OpenQuestion. The available authentication options are as follows:

- `use_email: true/false`. Authenticate with an email address and password. 
    Developers have to be added as registered users as described 
    [here](installation.md#adding-developers-and-administrators-as-users)
- `use_microsoft: true/false`. Authenticate with Microsoft.
- `use_google: true/false`. Authenticate with Google.
- `use_facebook: true/false`. Authenticate with Facebook.
- `use_token: true/false`. Users sign in by following a link in their email.
    Developers have to be added as registered users as described 
    [here](installation.md#adding-developers-and-administrators-as-users)

For more information on the above options in OpenQuestion, please see Anvil's documentation on
[authentication](https://anvil.works/docs/users/authentication_choices.html). 

