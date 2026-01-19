import streamlit as st
from QSEVA.controller.objeto_controller import ObjetoController


def registrar_objeto():
    descricao = None
    guardado_em = None
    id_colaborador = None
    data_hora_encontrado = None
    local_encontrado = None


    ObjetoController.inserir(
        descricao,
        guardado_em,
        id_colaborador,
        data_hora_encontrado,
        local_encontrado
    )