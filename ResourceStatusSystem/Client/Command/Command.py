""" The Command class is a simple base class for all the commands
    for interacting with the clients
"""

from DIRAC.ResourceStatusSystem.Utilities.Exceptions import *
from DIRAC.ResourceStatusSystem.Utilities.Utils import *

class Command(object):
  
  def __init__(self):
    self.args = None
    self.client = None
    self.RPC = None
    self.timeout = 10
  
  def setArgs(self, argsIn):
    """
    :params:

      :attr:`args`: a tuple 
        - `args[0]` should be a ValidRes

        - `args[1]` should be the name of the ValidRes

        - `args[2]` should be the present status
    """    
    self.args = argsIn
    if not isinstance(self.args, tuple):
      raise TypeError, where(self, self.setArgs)
    if self.args[0] not in ValidRes:
      raise InvalidRes, where(self, self.setArgs)

  def setClient(self, clientIn = None):
    """
    set `self.client`. If not set, a standard client will be instantiated.
    
    :params:
      :attr:`clientIn`: a client object 
    """
    self.client = clientIn
  
  def setRPC(self, RPCIn = None):
    """
    set `self.client`. If not set, a standard RPC will be instantiated.
    
    :params:
      :attr:`clientIn`: a client object 
    """
    self.RPC = RPCIn
  
  def setTimeOut(self, timoeut = None):
    """
    set `self.client`. If not set, a standard RPC will be instantiated.
    
    :params:
      :attr:`clientIn`: a client object 
    """
    self.timeout = timeout
  
  #to be extended by real commands
  def doCommand(self):
    """ 
    Before use, call at least `setArgs`.  
    """
    pass