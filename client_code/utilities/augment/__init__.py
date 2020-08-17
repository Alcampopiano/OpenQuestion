import anvil.microsoft.auth
import anvil.users
"""
    AnvilAugment
    Copyright 2020 Stu Cork

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Source code published at https://github.com/s-cork/AnvilAugment
"""

from anvil import js as _js

def add_event(component, event):
  """component: (instantiated) anvil component
  event: str - any jquery event string
  """
  if not isinstance(event, str):
    raise TypeError(f'event must be type str and not {type(event)}')
  _js.call_js('augment', component, event)
  
  
def set_event_handler(component, event, func):
  """component: (instantiated) anvil compoent
  event: str - any jquery event string
  func: function to handle the event
  """
  add_event(component, event)
  component.set_event_handler(event, func)
  

if __name__ == '__main__':
  print('AnvilAugment is a dependency')

