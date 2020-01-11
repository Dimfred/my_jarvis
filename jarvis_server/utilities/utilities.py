

# prints the function name and the values of the arguments
def print_func_deco( func ):
   def wrapper( *args, **kwargs ):
      print( "{}: {}".format( func.__name__, ", ".join( arg for arg in args ) ) )
      func( args )

   return wrapper