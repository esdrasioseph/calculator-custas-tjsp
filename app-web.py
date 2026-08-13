import streamlit as st
import time
from babel.numbers import format_currency

with open('./style.css') as s:
    st.markdown(f'<style>{s.read()}</style>', unsafe_allow_html= True)

st.set_page_config(page_title='Calculadora de Taxa Judiciária - TJSP', page_icon='⚖️')

st.title('Calculadora de Taxa Judiciária - TJSP')
st.text('Insira o valor da causa para calcular as custas iniciais devidas ao Tribunal de Justiça de São Paulo.')
st.text('Esse sistema deve ser utilizado apenas para o caso de protocolo de petições iniciais, '
'reconvenções e embargos (taxa de 1,5% conforme Lei Estadual nº 11.608/2003 do TJSP, respeitando os '
'limites de piso e teto.')
st.text('Esta calculadora é uma ferramenta auxiliar e não substitui a conferência das normas oficiais do TJSP. '
'O desenvolvedor não se responsabiliza por divergências ou recolhimentos indevidos.')

input_text = st.text_input('Valor da Causa (R$): ', placeholder='Ex.: 50.000,00 ou 50000')

if st.button('Calcular Custas', type='primary') or input_text:
    try:

        n1 = float(input_text.replace('.', '')
            .replace(',', '.')
            .replace('R$', '')
            .replace('reais', '')
            .strip())

        if (n1<= 0):
            st.error('Valor númerico inválido. Por favor, digite um número positivo maior que 0')

        valor = n1 * 0.015

        if valor <= 192.10:
            resultado_texto = "R$ 192,10 (Piso Mínimo)"
        elif valor > 115260:
            resultado_texto = "R$ 115.260,00 (Teto Máximo)"
        else:
            resultado_texto = format_currency(valor,'BRL', locale='pt_BR')

        with st.spinner('Calculando...'):
            time.sleep(1)

        st.success(f'O valor das custas iniciais é de {resultado_texto}.')

    except ValueError:
        st.error('Por favor, digite um valor númerico válido (Ex.: 50.000,00 ou 50000)')

st.markdown("""
<div class="footer">
    Desenvolvido por <a href="https://github.com/esdrasioseph" target="_blank">@esdrasioseph</a>
</div>
"""
,unsafe_allow_html= True)