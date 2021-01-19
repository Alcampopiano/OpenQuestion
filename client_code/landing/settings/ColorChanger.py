import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.js

def set_theme(theme_map):
  css = themed_css
  for name, value in theme_map.items():
    css = css.replace(f"%color:{name}%", value)
    
  anvil.js.call_js("setThemeCss", css)


# This is the subset of theme.css that is affected by theme colour choice.
# (I just copy-pasted theme.css and searched for theme:) 
  
themed_css = """
a, a:focus {
  color: %color:Primary 700%;
}

a:hover, a:active {
  color: %color:Primary 500%;
}


.left-nav a:hover, .left-nav .anvil-role-selected {
  color: %color:Primary 700%;
}

.app-bar {
  background-color: %color:Primary 500%;
}



.app-bar a:hover, .app-bar a:active {
  background-color: %color:Primary 700%;
}

.modal-footer .btn {
  color: %color:Primary 500%;
}

.btn, .btn-default, .file-loader>label {
  color: %color:Primary 500%;
}


.btn:hover, .btn:focus, .file-loader>label:hover {
  color: %color:Primary 500%;
}

/* , .btn:active:focus*/
.btn:active {
  color: %color:Primary 500%;
}

.anvil-role-primary-color > .btn, .btn-primary, .anvil-role-primary-color.file-loader>label {
  background-color: %color:Primary 500%;
}

.anvil-role-primary-color > .btn:hover, .anvil-role-primary-color > .btn:active, .anvil-role-primary-color > .btn:focus,
.btn-primary:hover, .btn-primary:active, .btn-primary:focus {
  background-color: %color:Primary 700%;
}

input.anvil-component:focus, .anvil-component select:focus, .anvil-datepicker input:focus {
  border-bottom: 2px solid %color:Primary 700%;
}

textarea.anvil-component:focus {
  border: 2px solid %color:Primary 700%;
}

.daterangepicker td.active {
  background-color: %color:Primary 500%;
}

.daterangepicker td.active:hover {
  background-color: %color:Primary 700%;
}

.daterangepicker .btn-success{
  color: %color:Primary 500%;
}
"""