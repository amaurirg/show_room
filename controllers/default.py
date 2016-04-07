# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def home():
    camera = '' 
    if request.vars.camera:
        camera = db(CAM.fabricante.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.modelo.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante)  | db(CAM.tipo.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.lente.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.resolucao.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.alcance_ir.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante)
    return dict(camera=camera)


def index():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    response.flash = 'Preencha os campos para acessar o sistema'
    auth.settings.remember_me_form = False
    #auth.messages.access_denied = 'Você não tem essa permissão!'
    #auth.messages.label_remember_me = "Lembrar-me"
    
    return dict(form=auth())

def home_admin():
    camera = '' 
    if request.vars.camera:
        camera = db(CAM.fabricante.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.modelo.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante)  | db(CAM.tipo.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.lente.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.resolucao.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.alcance_ir.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante)
    return dict(camera=camera)

def geral():
    camera = '' 
    if request.vars.camera:
        camera = db(CAM.fabricante.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.modelo.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante)  | db(CAM.tipo.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.lente.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.resolucao.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.alcance_ir.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante)
        lbl = H3('Câmera(s) Selecionada(s)', _class='test', _id=0)
    else:
        camera = db(CAM).select(orderby=CAM.fabricante)
        lbl = H3('Lista Geral de Câmeras', _class='test', _id=0)
    return dict(camera=camera, lbl=lbl)   

def geral_admin():
    camera = '' 
    if request.vars.camera:
        camera = db(CAM.fabricante.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.modelo.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante)  | db(CAM.tipo.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.lente.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.resolucao.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.alcance_ir.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante)
        lbl = H3('Câmera(s) Selecionada(s)', _class='test', _id=0)
    else:
        camera = db(CAM).select(orderby=CAM.fabricante)
        lbl = H3('Lista Geral de Câmeras', _class='test', _id=0)
    return dict(camera=camera, lbl=lbl)   

def novo_cadastro():
    camera = '' 
    if request.vars.camera:
        camera = db(CAM.fabricante.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.modelo.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante)  | db(CAM.tipo.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.lente.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.resolucao.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante) | db(CAM.alcance_ir.like('%'+request.vars.camera+'%')).select(orderby=CAM.fabricante)
        
        ##########################

        session.flash = camera
        
        ##########################

        redirect(URL('index_admin'))
    form = SQLFORM(CAM, submit_button = 'Cadastrar')
    if form.process().accepted:
        lbl = 'Câmera cadastrada com sucesso!'
    elif form.errors:
        lbl = 'Se houver algum campo vazio, preencha com hifen sem aspas: "-" !'
    else:
        lbl = 'Preencha os campos para cadastrar uma nova câmera!'
    
    return dict(camera=camera, form=form, lbl=lbl)



@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


