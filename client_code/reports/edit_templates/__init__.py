from ._anvil_designer import edit_templatesTemplate
from anvil import *
import anvil.server
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.microsoft.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import vega


class edit_templates(edit_templatesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    '''
// generate a static PNG image
function get_vega_png(spec){
  
	//var view = new vega.View(vega.parse(spec), {renderer: 'none'});
	var vega = require('vega');

	// create a new view instance for a given Vega JSON spec
	var view = new vega.View(vega.parse(spec), {renderer: 'none'});
  
	view.toCanvas()
  		.then(function(canvas) {
    	// process node-canvas instance
    	// for example, generate a PNG stream to write
    	var stream = canvas.createPNGStream();
  		})
  		.catch(function(err) { console.error(err); });
}    
    
    '''
    rows=anvil.server.call('get_templates')
    
    spec=rows[0]['templates']
    print(spec)
    view = vega.View(vega.parse(spec), {'renderer': 'none'})
    canvas = view.toCanvas()
    url_media = anvil.URLMedia(canvas.toDataURL())
    print(url_media.url)
    self.image_1.source=url_media
    print(url_media)
    #stream = canvas.createPNGStream()
    
    