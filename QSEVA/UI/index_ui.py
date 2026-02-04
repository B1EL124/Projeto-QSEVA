import streamlit as st


class IndexUI:
    @classmethod
    def main():
        st.session_state.usuario = st.session_state.get("usuario", None)
        st.session_state.perfil = st.session_state.get("perfil", None)

        if st.session_state.usuario is None:
            # loginUI.main()
            ...