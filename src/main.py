# -*- coding: utf-8 -*-

from model.model import Model
from controller.controller import Controller


if __name__ == '__main__':
    ip = 'localhost'
    user = 'gabriel'
    pswd = 'olescki'
    db = 'Pronondb'

    m = Model(ip, user, pswd, db)
    c = Controller(m)
    c.run()
