from ._anvil_designer import drop_downTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class drop_down(drop_downTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.tag.logic=None
    self.tag.logic_target_ids=[]
    self.tag.current_value=None

  def drop_down_change(self, **event_args):
    
    self.tag.current_value=self.drop_down.selected_value
    
    form_dict=get_open_form().tag.form_dict
    
    for widget_id in self.tag.logic_target_ids:
      
      logic=form_dict[widget_id].tag.logic
      print('func', logic['func'])
      
      truth_array=[]
      for condition in logic['conditions']:
        
        source_comp=form_dict[condition['id']]
        test_val=condition['value']
        actual_val=source_comp.tag.current_value
        
        print('comparison', condition['comparison'])
        print('test_val', test_val)
        print('actual_val', actual_val)
        comparison=condition['comparison']
        
        if condition=='>':
          truth_array.append(test_val>actual_val)
          
        elif condition=='<':
          truth_array.append(test_val<actual_val)
          
        elif condition=='=':
          truth_array.append(test_val==actual_val)
          
        elif condition=='!=':
          truth_array.append(test_val!=actual_val)
          
        elif condition=='<=':
          truth_array.append(test_val<=actual_val) 
          
        elif condition=='>=':
          truth_array.append(test_val>=actual_val)
          
      print('truth array', truth_array)
      print('any', any(truth_array))
      print('all', False if not truth_array else all(truth_array))
      
        

