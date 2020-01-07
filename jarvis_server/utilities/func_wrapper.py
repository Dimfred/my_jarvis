class func_wrapper:

   def __init__( self, func, *args ):

      self.__func = func
      self.__args = args


   def exe(self):

      self.__func( *self.__args )
