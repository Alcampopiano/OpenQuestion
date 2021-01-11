# Survey Development

## Survey dashboard
The survey dashboard allows you to edit, build, and configure [settings](settings.md) for your surveys. 
Survey data and share links can also be accessed from the dashboard. Clicking "New survey"
or the :pencil: icon will take you to the survey designer (explained below) for a new or
existing survey, respectively.

**The survey dashboard**
![dash](img/dash.png)

## Survey designer
The survey designer is where most of the survey development takes place. It consists of the 
[designer toolbar](survey_dev.md#designer-toolbar) (click on the :wrench: to 
toggle the side panel's visibility) and various other
UI elements, including those that allow you to structure 
your survey and control how it behaves. To preview the survey as the end user would see it,
click "Preview" at the top of the page (or access the share link from the dashboard).

**The survey designer**
![design](img/design.gif)

## Designer toolbar
The designer toolbar contains widgets (e.g., text_box, drop_down, sections, etc). Clicking on the widgets 
adds them to the page below the currently selected element. The :wrench: icon will toggle the
toolbar's visibility.

**The designer toolbar**
![design](img/des_tool.gif)

## Widget settings
When a widget is added to the page during survey development, values need to be specified
to control how the widget appears to the end user.

For example, the text_box widget (as shown above) requires the following information:

- title 
    - For example, "What is your name?"
    
- placeholder 
    - text that prompts the user. For example, "Type your name here?"
   
- mandatory flag
    - if checked, this field must be filled out by the user before the survey can be submitted
    
- number
    - if checked, this field will be restricted to a number
    
All widgets have their own sets of options to be specified. Please click [here](widgets.md) 
to learn about the available widgets and how they are used.

!!! tip "Are widget settings represented as key/value pairs?"
    Yes! In fact, all survey settings are represented by an underlying 
    and accessible [JSON/Python dict](as_json.md) where keys and values
    corresspond exactly to what is shown in the designer

## Widget toolbar
Once a widget has been added to the page, the widget's toolbar can be used to move the widget up or down,
delete the widget, and control the widget's visibility with [branching](survey_dev.md#branching).

**The widget toolbar**
![design](img/wid_tool.gif)

## Basic Widget controls
The :minus: sign can be used to delete the widget and the up/down arrows can be used
to move the widget up or down.

## Branching
The :git: icon opens up the branching UI. Branching controls the visibility
of the selected widgets (including sections) based on the values of other widgets.
Multiple conditions can be combined together to make complex branching rules if needed.
The below example shows a text_box widget's visibility being controlled by the 
value of a slider widget. In this case, whenever the slider goes below 40, 
the text_box is displayed. When branching exists on a widget, the :git: icon
on the widget's toolbar is highlighted. 

**Setting branching rules on a text_box**
![bran_rule](img/bran_ui.gif)

**The text_box is revealed when the condition is met**
![bran_proof](img/bran_proof.gif)
