# -*- coding: utf-8 -*-

#CAM (cameras)
CAM.fabricante.requires = IS_NOT_EMPTY()
CAM.modelo.requires = IS_NOT_EMPTY()
CAM.tipo.requires = IS_NOT_EMPTY()
CAM.tec.requires = IS_NOT_EMPTY()
CAM.lente.requires = IS_NOT_EMPTY()
CAM.angulo.requires = IS_NOT_EMPTY()
CAM.resolucao.requires = IS_NOT_EMPTY()
CAM.wdr_blc.requires = IS_NOT_EMPTY()
CAM.alcance_ir.requires = IS_NOT_EMPTY()
CAM.consumo.requires = IS_NOT_EMPTY()
CAM.grau.requires = IS_NOT_EMPTY()
CAM.int_ext.requires = IS_NOT_EMPTY()
CAM.ip.requires = IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'cameras.ip')
CAM.onvif.requires = IS_NOT_EMPTY()
CAM.usuario.requires = IS_NOT_EMPTY()
CAM.senha.requires = IS_NOT_EMPTY()
CAM.serial.requires = IS_NOT_EMPTY()
CAM.switch_poe.requires = IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'cameras.switch_poe')

