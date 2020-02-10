#!/usr/bin/python3
import logging as log
log.basicConfig(level=log.DEBUG)
log.info( "App startup." )


import jarvis

if __name__ == "__main__":
   jarvis.start()
