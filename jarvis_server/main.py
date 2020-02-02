#!/usr/bin/python3

import tasks.action_performer
import tasks.app_msg_recv
import tasks.discovery

import logging as log


if __name__ == "__main__":

   log.basicConfig(level=log.INFO)
   log.info( "App startup." )


   tasks.discovery.start()

   tasks.action_performer.start()

   tasks.app_msg_recv.start( tasks.action_performer.push_queue )

