import streamlit as st
import matplotlib.pyplot as plt

def get_contact_table():
    contacts = {
        "Nome": [
            "Alexandre Veira Pereira Pacelli",
            "Matheus Lima Gravino Passos",
            "Moisés Paulo dos Santos Júnior",
            "Samuel Paiva Bernardes",
            "Thiago de Almeida Lopes",
            "Gabriella",
            "Camila",
            "Marcos",
        ],
        "Telefone": [
            "32988757437",
            "22999634438",
            "32999487556",
            "31996750597",
            "24981157097",
            "",
            "",
            "",
        ],
        "Email": [
            "alexandrevpp@gmail.com",
            "matheusinglp@hotmail.com",
            "moisespaulo258@gmail.com",
            "samuelpbernardes@yahoo.com.br",
            "thiago9863",
            "",
            "",
            "",
        ],
    }        

    return contacts

def get_staff_members():
    members = {
        'Nomes': [
            'Alexandre',
            'Camila',
            'Gabriella',
            'Matheus',
            'Thiago',
            'Moisés',
            'Marcos',
            'Vanderlei',
            'Lucas',
            'Samuel',
            'Wagno',
            'Renan',
        ],
        'Data de efetivação': [
            '2018',
            '25/7/2020',
            '29/8/2020',
            '2017',
            '2017',
            '2019',
            '',
            '2019',
            '2020',
            '2017',
            '30/12/2020',
            '24/12/2020',
         ],
        'Data de saída': [
            '',    
            '',    
            '29/10/2020',
            '',    
            '',    
            '22/08/2020',
            '',    
            '2019',
            '29/8/2020',
            '13/06/2020',
            '',    
            '',    
        ]
    } 

    return members
    
def get_flow_data():
    flow_data_total = {
        'Nome': [
            'Samuel',
            'Matheus',
            'Alexandre',
            'Thiago',
            'Moisés',
        ],
        'Valor': [
            0,
            10,
            0,
            0,
            0,
        ]
     }

    flow_data_month = {
        'Nome': [
            'Samuel',
            'Matheus',
            'Alexandre',
            'Thiago',
            'Moisés',
        ],
        'Valor': [
            0,
            8,
            0,
            0,
            0,
        ],
     }

    return flow_data_total, flow_data_month


def projects_page():
   st.selectbox('Projetos', [
        'EuVi'
    ])

   st.selectbox('Mês:',['Maio'])

   st.header('Integrantes')
   st.table(get_staff_members())
   flow_data_total, flow_data_month = get_flow_data()
   st.header('Fluxo')
   col1, col2 = st.beta_columns(2)

   col1.header('Mensal')
   col1.table(flow_data_month)
   col1.subheader('Gasto mensal: R$ 8,00')

   col2.header('Total')
   col2.table(flow_data_total)
   col2.subheader('Gasto total: R$ 10,00')

   st.header('Contribuição geral')
   
   plt.style.use('bmh')
   pie_fig = plt.figure()
   plt.pie(
    x=[
        0.1,
        10,
        0.1,
        0.1,
        0.1,
      ],

    labels=[
        'Samuel',
        'Matheus',
        'Alexandre',
        'Thiago',
        'Moisés',
      ]
   )
   st.pyplot(pie_fig)


def home_page():
    st.markdown("# Bem vindo a plataforma Digitalize")
    st.markdown("")


def contact_page():
    st.header('Contatos')
    st.table(get_contact_table())

if __name__ == '__main__':
    st.title('Digitalize')

    pages = {
            'Inicio': home_page,
            'Contatos': contact_page,
            'Projetos': projects_page
            }
    option = st.sidebar.selectbox("Navegação", [
        "Inicio", "Contatos", "Projetos",
        ])

    pages[option]()
