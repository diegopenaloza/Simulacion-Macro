import numpy as np
import streamlit as st
import plotly.graph_objects as go

# import streamlit.components.v1 as components  # Import Streamlit

# # Render the h1 block, contained in a frame of size 200x200.
# components.html("<html><body><h1>Hello, World</h1></body></html>")

tee="# Dinámica de los precios de las materias primas de la expansión monetaria en una economía abierta"
tee
te="### (Simulación incremento de la oferta monetaria ( $$m$$ ) en el largo plazo ) "

te
st.markdown(""" **Autores**: Diego Peñaloza , Wilson Chafla , Kevin Narvaez """)
st.markdown("""** Fecha** :  19 de diciembre de 2020""")
st.markdown("""** Asignatura ** :  Macroeconomía III""")

st.markdown("""

Partiendo del diagrama de fase , hemos plasmado unicamente la senda de solución en el largo plazo
,ya que esta nos permite observar el sobreajuste de los precios , en primera instancia se partira de 
un beta igual a 100, conlos parametros propùestos , una oferta monetaria de 5 , que podra se modificada 
en la simulación.

""")


st.markdown("""

El equilibrio inicial está en Q_0 en la línea (2); los precios 
iniciales de manufactura y agricultura son Pm_0 y P_c_0, respectivamente. 
Para simplificar nuestro análisis gráfico, asumimos inicialmente Pm_0 = P_c_0 y,
 por lo tanto, Q_0 está ubicado en una línea de 45 ° que pasa por el origen.


""")



st.markdown("""

Tras un aumento permanente no anticipado de la oferta monetaria, la línea 
(1) se desplaza hacia la derecha a (2).Esto se puede llevar acabo moviendo el primer slider 
llamado m , que parte de una oferta monetaria de 5 (en millones)unidades monetarias, 
hacia la derecha  .
  Dado que la neutralidad monetaria  es válida a largo plazo, el punto $$Q^*$$, donde la línea (2)
  interseca la línea de 45 °,
 es el nuevo punto de equilibrio. Debido a que los precios de los productos manufacturados 
 se ajustan con un desfase temporal, los precios de los productos agrícolas en
  consecuencia deben subir inmediatamente de pc_0  a p'c , y la economía saltará 
  verticalmente de Q_0 a Q'  en el instante de expansión monetaria. 
  A partir de entonces, los precios agrícolas seguirán cayendo y los precios de 
  las manufacturas seguirán subiendo a medida que la economía se mueva a 
lo largo de la rama estable (2) hacia su nuevo equilibrio estacionario Q *.

""")



gyu="Slider $m$"
gyu
s=" "
v=st.slider(s,2,10,5)

m=v
ss1="Slider $\\beta$"
ss=" "
ss1
vv=st.slider(ss,1,100,100)


beta=vv
pm=np.linspace(1,20)
pi=0.1
delta=1.2
alpha_1=0.6
psi=0.4
alpha_2=0.2
alpha_3=0.2
x=0.29
theta=0.13

k=(beta*(psi*alpha_1+(delta+psi)*alpha_3))/((x+theta)*psi)

eta=0.1
phi=0.2


v=(eta*alpha_3+phi*psi)/psi

y=5
rho=0.1
c=0.05
sigma=2
i=0.05
lamda=5

p_ast_m=3.75

tilde_p_c=m-v*y+k*(rho-c)+(((lamda*psi-sigma*alpha_3)/(psi))-k)*i
# tilde_p_c

Theta_1=-0.29
Theta_2=-0.14
Theta_3=0.001

t=np.linspace(0,20,20)

H1=1
H2=0.4
H3=0.2

prt1=(x+theta)*(alpha_3-Theta_1*lamda)+Theta_1*alpha_1*beta

prt2=(x+theta)*(alpha_3-Theta_1*lamda)-Theta_1*beta*(1-Theta_1*lamda-alpha_1)

p_c_s1=tilde_p_c+((prt1)/(prt2))*H1*np.exp(Theta_1*t)



prt3=(x+theta)*(alpha_3-Theta_2*lamda)+Theta_2*alpha_1*beta

prt4=(x+theta)*(alpha_3-Theta_2*lamda)-Theta_2*beta*(1-Theta_2*lamda-alpha_1)

p_c_s2=((prt3)/(prt4))*H2*np.exp(Theta_2*t)



prt5=(x+theta)*(alpha_3-Theta_3*lamda)+Theta_3*alpha_1*beta

prt6=(x+theta)*(alpha_3-Theta_3*lamda)-Theta_3*beta*(1-Theta_3*lamda-alpha_1)

p_c_s3=((prt5)/(prt6))*H3*np.exp(Theta_3*t)


p_c_sT=tilde_p_c+p_c_s1+p_c_s2+p_c_s3

cr=prt1/prt2

# cr
cr2=prt3/prt4
# cr2

cr3=prt5/prt6
# cr3

# tilde_p_c
# p_c_s1
# p_c_s2
# prt3/prt4

w=(beta*(delta*alpha_1+(delta+psi)*alpha_2))/((x+theta)*psi)
e=m-(v-(eta/psi))*y-p_ast_m-w*(rho-c)+(w+(lamda+(sigma/psi))*(alpha_1+alpha_2))*i
A=(pi*sigma)/(1-pi*sigma)
u=(sigma*alpha_3*(x+theta)+beta*delta)/((x+theta)*psi)
tilde_p_m=m-v*y-((beta*(psi*alpha_2-delta*alpha_3))/((x+theta)*psi))*(rho-c)+(lamda+w-u)*i

pc=(tilde_p_c)+ cr*(pm-tilde_p_m)

# tilde_p_m

# tilde_p_c
# cr

pm_0=(tilde_p_c-cr*tilde_p_m)/(-cr+1)


pc=(tilde_p_c)+ cr*(pm-tilde_p_m)

pc2=(tilde_p_c)+ cr*(3.9499999999-tilde_p_m)

import plotly.graph_objects as go



pm=np.linspace(0,10)
# pc=5.16-0.30*pm
fig = go.Figure()
# fig.add_trace(go.Scatter(x=pm, y=pc,
#                     mode='lines',
#                     name='lines'))

fig.add_trace(go.Scatter(x=pm, y=pm,
                    mode='lines',
                    name='$e$'
                    ,
                     line = dict(color='black', width=1, dash='dot')
                     ))


fig.add_trace(go.Scatter(x=[pm_0,pm_0], y=[0,pm_0],
                    mode='lines',
                    name='recta6',
                    line = dict(color='blue', width=1, dash='dot')
                    ))


fig.add_trace(go.Scatter(x=[3.9499999999999993,3.9499999999999993], y=[0,pc2],
                    mode='lines',
                    name='recta22',
                    
                     line = dict(color='green', width=1, dash='dot')
                    ))



fig.add_trace(go.Scatter(x=[pm_0,pm_0], y=[0,pm_0],
                    mode='lines',
                    name='recta'
                    ,
                    line = dict(color='red', width=1, dash='dot')
                    ))



fig.add_trace(go.Scatter(x=[0,pm_0], y=[pm_0,pm_0],
                    mode='lines',
                    name='recta4',
                    
                    line = dict(color='red', width=1, dash='dot')
                    ))

fig.add_trace(go.Scatter(x=[0,3.9499999999999993], y=[3.9499999999999993,3.9499999999999993],
                    mode='lines',
                    name='recta4',
                    
                    line = dict(color='black', width=1, dash='dot')
                    ))


fig.add_trace(go.Scatter(x=[0,3.9499999999999993], y=[pc2,pc2],
                    mode='lines',
                    name='recta78',
                    
                    line = dict(color='green', width=1, dash='dot')
                    ))

pc_a=(tilde_p_c)+ cr*(pm-tilde_p_m)
fig.add_trace(go.Scatter(x=pm, y=pc_a,
                    mode='lines',
                    name='Variacion'))


if beta>1:

    pc_s=(3.9499999999999993)-0.3074361003257089*(pm-3.9499999999999975)
    fig.add_trace(go.Scatter(x=pm, y=pc_s,
                        mode='lines',
                        name='45º  ',
                        
                        ))

else:
    pc_s=(3.9499999999999993)+0.42212281415209435*(pm-3.9499999999999975)
    fig.add_trace(go.Scatter(x=pm, y=pc_s,
                        mode='lines',
                        name='Inicial',
                        ))




fig.update_xaxes(
    range=[-5,15],  # sets the range of xaxis
    # constrain="domain",  # meanwhile compresses the xaxis by decreasing its "domain"
)
fig.update_yaxes(

    range=[-5,15],  # sets the range of xaxis

)

fig.update_layout(
    title="Precios P.Agricolad vs Precios P.Manufacturados",
    legend=dict(
    orientation="h",
    yanchor="bottom",
    y=-0.2,
    xanchor="right",
    x=0.7
),
    autosize=False,
    width=900,
    height=600,
        margin=dict(
        l=0
    ),
        xaxis_title="Precio de Productos Manufacturados",
    yaxis_title="Precio de Productos Agricolas",
    template="plotly_white",
    showlegend=False,
)

# plotly_white

fig.update_yaxes(nticks=20)
fig.update_xaxes(nticks=20)

fig.update_xaxes(range=[-2, 12])
fig.update_yaxes(range=[-1, 13])
# fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
# fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='black')
fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='black')


pm_g=np.arange(1,10,0.5)
pc_a_g=(tilde_p_c)+ cr*(pm_g-tilde_p_m)

for i, j in zip(pc_a_g,pm_g):
    if j<pm_0 and j>3.949999999999:
        fig.add_annotation(x=j, y=i,
                text="➤",
                showarrow=False,
                # yshift=5,
                font=dict(size=16,
                ),
                textangle=5
                      
        
                )

    # else:
    #     fig.add_annotation(x=j, y=i,
    #         text="➤",
    #             showarrow=False,
    #             # yshift=5,
    #             font=dict(size=16,
    #             ),
    #             textangle=200
    #             )
                
       
dfg="$Pm_0$"


fig.add_annotation(x=pm_0, y=pm_0,
            text="🔴",
            showarrow=False,
            )

fig.add_annotation(x=pm_0, y=pm_0+0.8,
            text="Q*",
            showarrow=False,
                    font=dict(
            family="Courier New,bold",
            size=20,
            color="black"
            ),
                    align="center",

        ax=20,
        ay=-30,
        bordercolor="#c7c7c7",
        # borderwidth=6,
        borderpad=4,
        bgcolor="#ff7f0e",
        opacity=0.8
            )

if pc_a[-1]>2.1900115930:

    fig.add_annotation(x=10.3, y=pc_a[-1],
                text="(2.1)",
                showarrow=False,
                )
else:
    fig.add_annotation(x=10.3, y=2.0900115930,
                text="(2)",
                showarrow=False,
                )

fig.add_annotation(x=10.3, y=2.0900115930,
                text="(2)",
                showarrow=False,
                )

fig.add_annotation(x=3.949999999, y=-0.7,
                text=" Pm_0 ",
                showarrow=False,
                yshift=10)
if pm_0<4 and pm_0>3:
    fig.add_annotation(x=pm_0, y=-0.7,
                text=" Pm_0 ",
                showarrow=False,
                yshift=10)
else:
    fig.add_annotation(x=pm_0, y=-0.7,
                text=" Pm_1 ",
                showarrow=False,
                yshift=10)


if pm_0>4 or pm_0<3.8 :

    fig.add_annotation(x=-0.5, y=pm_0,
                    text=" Pc_1 ",
                    showarrow=False,
                    )

fig.add_annotation(x=-0.5, y=3.9499999999999993,
                text=" Pc_0 ",
                showarrow=False,
                )

if pm_0>4 or pm_0<3.8 :

    fig.add_annotation(x=-0.5, y=pc2,
                text=" P'c ",
                showarrow=False,
                )


fig.add_annotation(x=3.9499999999999993, y=pc2,
            text="🔵",
            showarrow=False,
            )

fig.add_annotation(x=3.9499999999999993, y=pc2+0.8,
            text="Q'",
            showarrow=False,
                    font=dict(
            family="Courier New,bold",
            size=20,
            color="black"
            ),
                    align="center",

        ax=20,
        ay=-30,
        bordercolor="#c7c7c7",
        # borderwidth=6,
        borderpad=4,
        bgcolor="#ff7f0e",
        opacity=0.8
            )



fig.add_annotation(x=3.9499999999999993, y=3.9499999999999993,
            text="🟢",
            showarrow=False,
            )

fig.add_annotation(x=3.9499999999999993, y=4.7499999999999993,
            text="Q_0",
            showarrow=False,
                    font=dict(
            family="Courier New,bold",
            size=20,
            color="black"
            ),
                    align="center",

        ax=20,
        ay=-30,
        bordercolor="#c7c7c7",
        # borderwidth=6,
        borderpad=4,
        bgcolor="#ff7f0e",
        opacity=0.8
            )


st.plotly_chart(fig, filename='latex',include_mathjax='cdn')





st.markdown("""

Como se analizo en el trabajo , tambien se puede presentar otra situación  en la que está presente una 
subestimación de los precios agrícolas.
 De la ecuación (10) se desprende claramente que la senda de solución puede tener pendiente ascendente.
 En nuestra simulación esto se puede ver reflejado en su totalidad cuando el $$\\beta$$ disminuya su valor a 1 , 
 esto es existe menor sustituibilidad en tre bonos y productos agricolas,
 Esto se puede lograr al mover el slider  .

 En respuesta a un aumento en la oferta monetaria, los precios agrícolas, en el impacto, subirán de pc_0 a p'c
  y luego continuarán aumentar hasta que se alcance su valor a largo plazo, pc_1.
   Esto se puede lograr de igual manera que en la ocasion anterior 
   moviendo el slider m hacia la derecha. 
""")
import base64

# st.markdown("![Alt Text](vid.gif)")

# file_ = open("vid.gif", "rb")
# contents = file_.read()
# data_url = base64.b64encode(contents).decode("utf-8")
# file_.close()

st.markdown("**Referencia de Funcionamiento**") 
st.image("vid.gif",output_format="GIF")

st.markdown("**Codigo que se uso para esta simulación :**") 

import webbrowser
url = 'https://github.com/Dipg/Simulacion-Macro/blob/main/plt.py'

if st.button('Codigo '):
    webbrowser.open_new_tab(url)