# Import the pandas library.
import pandas

# Read in the data.
data = pandas.read_csv("dump.csv")

#quitar filas de profesores
data = data[data["perfil"] != "profesor"]

#pasar datos del csv al dataframe
df = pandas.DataFrame(data)
df = df.sort_values(by=['id_usuario', 'date', 'time'])

#agrupar por id_usuario
df_by_idusuario = df.groupby('id_usuario')
   
# Check type of GroupBy object
# print(type(df_by_idusuario))

#print(df_by_idusuario.describe())

#for index, df_usuario in df.groupby('id_usuario'):
#    print(df_usuario.groups)
    #print(df_usuario)

print(list(df_by_idusuario)[3])