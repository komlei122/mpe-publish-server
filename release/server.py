# -*- coding: utf-8 -*-

import web
import sys
import os
import logging, logging.config
# log
logging.config.fileConfig("./config/logger.cfg")
logger = logging.getLogger("logger01")

# sys
reload(sys)
sys.setdefaultencoding('utf-8')


urls = (
    '/(.*)', 'Global'
)

# render = web.template.render('docs')

app = web.application(urls, globals())

class Global:
    def GET(self,name):
        if not name:
            name ='index.html'
        real_path=os.path.join('docs',name)
        f = open(real_path, "r")
        context=f.read()
        return context

if __name__ == "__main__":
    # web.config.debug = False
    web.config.debug = True
    logger.info('start server ...')
    app.run()
    logger.info('stop server ...')
