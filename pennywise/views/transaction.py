# -*- coding: utf-8 -*-

from pennywise import app

@app.route('/transaction/<uuid>/')
def transactionview(uuid):
    return "Transaction: %s" % uuid
