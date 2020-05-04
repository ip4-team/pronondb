# -*- coding: utf-8 -*-

from model.model import Model
from controller.controller import Controller


if __name__ == '__main__':
    ip = 'localhost'
    db = 'Pronondb'
    #  user = 'gabriel'
    #  pswd = 'olescki'

    c = Controller(ip, db)
