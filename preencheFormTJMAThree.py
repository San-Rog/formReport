import streamlit as st 
import pymupdf 
import os
import time

def createForm():
    doc = pymupdf.open(formPdf)
    docNew = 'template.pdf' 
    if optionsCred[0] in obj:
        markCp = 'x'
    else:
        markCp = ''
    if optionsCred[1] in obj:
        markHc = 'x'
    else:
        markHc = ''
    if optionsCred[2] in obj:
        markHs = 'x'
    else:
        markHs = ''
    if modelOne:
        markCC = 'x'
    else:
        markCC = ''
    if modelTwo:
        markCP = 'x'
    else:
        markCP = ''    
    dados = [[(141.14398193359375, 1.04*267.00738525390625, 537.1439819335938, 280.29644775390625),precat],
              [(145.3800048828125, 1.04*282.80743408203125, 523.3800048828125, 296.09649658203125), requer],
              [(268.5360412597656, 1.04*298.7073974609375, 520.5360107421875, 311.9964599609375), proc],
              [(1.02*108.68399047851562, 1.03*377.90740966796875, 378.6839904785156, 391.19647216796875), bank],
              [(1.05*127.67999267578125, 1.03*393.8074035644531, 181.67999267578125, 407.0964660644531), agency],
              [(1.02*197.77198791503906, 1.03*393.8074035644531, 215.77198791503906, 407.0964660644531),  verify],
              [(1.03*401.00408935546875, 1.03*393.8074035644531, 509.00408935546875, 407.0964660644531), count],
              [(519.0000610351562, 1.03*393.8074035644531, 537.0000610351562, 407.0964660644531), countV],
              [(1.1*96.36000061035156, 1.03*409.607421875, 258.3599853515625, 422.896484375), cpf],
              [(1.02*262.3559875488281, 1.03*409.607421875, 298.3559875488281, 422.896484375), cpfV],
              [(1.02*422.2760314941406, 1.025*473.0074157714844, 440.2760314941406, 486.2964782714844), edital],
              [(1.04*89.56800079345703, 1.02*488.90740966796875, 107.56800079345703, 502.19647216796875), f'{rodada}.'],
              [(1.02*261.760009765625, 1.018*661.2073974609375, 279.760009765625, 674.4964599609375), '14'],
              [(1.02*306.06402587890625, 1.018*661.2073974609375, 324.06402587890625, 674.4964599609375), '07'],
              [(1.02*353.3680419921875, 1.018*661.2073974609375, 389.3680419921875, 674.4964599609375), '2025'],
              [(1.02*119.80000305175781, 1.031*330.40740966796875, 123.79609680175781, 343.69647216796875), markCp],
              [(1.015*219.04002380371094, 1.031*330.40740966796875, 223.03611755371094, 343.69647216796875), markHc],
              [(1.009*348.3881530761719, 1.031*330.40740966796875, 352.3842468261719, 343.69647216796875), markHs],
              [(1.01*259.6679992675781, 1.028*393.8074035644531, 263.6640930175781, 407.0964660644531), markCC],
              [(1.013*318.63604736328125, 1.028*393.8074035644531, 322.63214111328125, 407.0964660644531), markCP]]
    for dado in dados:
        pos = dado[0]
        text = dado[1]
        page_number = 0
        cor = (0, 0, 1) 
        page = doc.load_page(page_number)
        rect = pymupdf.Rect(pos)  
        rotate = 0  
        shape = page.new_shape()
        shape.insert_text(rect.top_left, text, color=cor, rotate=rotate)
        shape.commit()
        doc.save(docNew)
    doc.close()
    with open(docNew, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    return PDFbyte
    
def iniKeys(mode, key):
    if mode == 0:
        for key in keysCount:
            if key not in st.session_state:
                st.session_state[key] = False
 
def message(head, text):
    @st.dialog(head)
    def config():
        st.markdown(text)
    config()

def zeraWidget(opt):
    if opt == 0:
        for k, key in enumerate(allKeys):
            print('key', key)
            if key not in st.session_state:
                if k == 3:
                    st.session_state[key] = []
                elif k in [7, 8]:
                    st.session_state[key] = False
                elif k == 13:
                    st.session_state[key]  = 0
                else:
                    st.session_state[key] = ''        
    else:
        for k, key in enumerate(allKeys):
            del st.session_state[key] 
            if k == 3 or k == 13:
                st.session_state[key] = []
            elif k in [7, 8]:
                st.session_state[key] = False
            elif k == 13:
                st.session_state[key]  = 0
            else:
                st.session_state[key] = ''    

def ckeckPlaces(): 
    placeVoid = False
    #precat, requer, proc, obj, modelOne, modelTwo, bank, agency, verify, cpf, cpfV, edital, rodada, count, countV
    for e, elem in enumerate([precat, requer, proc, obj, bank, agency, verify, cpf, cpfV, edital, rodada, count, countV]):
        if type(elem) == list:
            if len(elem) == 0:
                placeVoid = True
                break
        else:
            if len(elem.strip()) == 0:
                placeVoid = True
                break
        st.write(e, elem, placeVoid)
    if all([not modelOne, not modelTwo]): 
        placeVoid = True
    return placeVoid            

def main():
    global formPdf, precat, requer, proc, obj, modelOne, modelTwo, bank, agency, verify, cpf, cpfV, edital, rodada, count, countV
    global day, mont, year, keysCount
    global optionsCount, optionsCred
    global allKeys 
    allKeys = ['prc', 'req', 'process', 'credyt', 'banker', 'num_agency', 'digit_agency', 
              'count_cc', 'count_cp', 'num_count', 'digit_count', 'num_cpf', 'digit_cpf', 
              'num_xxxx', 'num_yyyy']
    optionsEdit = [str(n) for n in range(1, 5)]
    optionsRod = [str(n) for n in range(1, 5)]
    #iniKeys(0, '')
    optionsCred = ["Crédito Principal", "Honorários Contratuais", "Honorários Sucumbenciais"] 
    optionsCount = ["Conta-Corrente", "Conta-Poupança"]   
    zeraWidget(0)
    formPdf = 'formTJMA.pdf'
    formPdf, precat, requer, proc, obj, modelOne, modelTwo, bank, agency, verify, cpf, cpfV, edital, rodada, count, countV = ['' for w in range(16)]
    formPdf = 'formTJMA.pdf'
    with st.container(border=2):
        colPrecat, colBank, colTerm = st.columns([2.4, 2, 2], gap='small', vertical_alignment='center')
        with colPrecat:
            precat = st.text_input('Precatório n°', key=allKeys[0], value=st.session_state[allKeys[0]])
            requer = st.text_input('Requerente(s)', key=allKeys[1], value=st.session_state[allKeys[1]])
            proc = st.text_input('Referência (Ação Originária/Execução)', key=allKeys[2], value=st.session_state[allKeys[2]])
            obj = st.multiselect('Crédito Negociado', optionsCred, default=st.session_state[allKeys[3]], key=allKeys[3])
        with colBank:
            bank = st.text_input('Banco',  key=allKeys[4], value=st.session_state[allKeys[4]])
            colAgency, colDigit = st.columns([6.2, 2])
            agency = colAgency.text_input('Agência', key=allKeys[5], value=st.session_state[allKeys[5]])
            verify = colDigit.text_input('Dígito', key=allKeys[6], value=st.session_state[allKeys[6]])
            st.caption('')
            colOne, colTwo = st.columns(spec=2)
            modelOne = colOne.checkbox(optionsCount[0], key=allKeys[7], value=st.session_state[allKeys[7]])
            modelTwo = colTwo.checkbox(optionsCount[1],  key=allKeys[8], value=st.session_state[allKeys[8]])
            colCount, colCountV = st.columns([6.2, 2])
            count = colCount.text_input('Conta',  key=allKeys[9], value=st.session_state[allKeys[9]])
            countV = colCountV.text_input('Final',  key=allKeys[10], value=st.session_state[allKeys[10]])
        with colTerm:
            st.write(st.session_state[allKeys[13]])
            cod, codV = st.columns([6.2, 2])
            cpf = cod.text_input('CPF', key=allKeys[11], value=st.session_state[allKeys[11]])
            cpfV = codV.text_input('Verificador', key=allKeys[12], value=st.session_state[allKeys[12]])
            edital = st.selectbox('Edital Conjunto TJMA/PGE-MA_2025', optionsEdit, key=allKeys[13], index=st.session_state[allKeys[13]])
            rodada = st.selectbox('Edital da Rodada de Chamamento n.°', optionsRod, key=allKeys[14])
    if modelOne and modelTwo:
        del st.session_state[allKeys[7]]
        del st.session_state[allKeys[8]]
        #iniKeys(0, keysCount[1])
        message('Dupla marcação de contas bancárias', 'Assinale apenas conta-corrente ou conta-poupança!')
        time.sleep(3)
        st.rerun() 
    pdfCreate = ''  
    with st.container():
        colCreate, colDown, colClear = st.columns(spec=3)    
        if colCreate.button('Preenchimento'):
            if ckeckPlaces(): 
                message('Campos vazios', 'Preencha todos os campos!')
                time.sleep(3)
            else:
                pdfCreate = createForm()
                if len(pdfCreate) > 0:
                    colDown.download_button(
                                    label='Download',
                                    data=pdfCreate,
                                    file_name='formulário_TJMA_preenchido.pdf',
                                    mime='application/octet-stream',
                    )     
                    zeraWidget(1)
                
if __name__ == '__main__':
    st.set_page_config(layout="wide")
    main()
