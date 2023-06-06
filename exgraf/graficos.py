from util import bd
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/barras')
def barras():
   # Recuperando Tipos de Software existentes na base de dados
   mysql = bd.SQL("root", "uniceub", "test")
   comando = "SELECT nme_tipo, COUNT(idt_software) AS qtd FROM tb_tipo JOIN tb_software ON idt_tipo=cod_tipo GROUP BY nme_tipo;"

   cs = mysql.consultar(comando, ())

   grf = ""
   for [nome, qtd] in cs:
       grf += ", ['" + nome + "', " + str(qtd) + ", '#9999FF']"
   cs.close()

   return render_template('barras.html', barras=grf)


@app.route('/org')
def org():
   # Recuperando Tipos de Software existentes na base de dados
   mysql = bd.SQL("root", "uniceub", "test")
   comando = "SELECT * FROM tb_tipo ORDER BY nme_tipo;"

   cs = mysql.consultar(comando, ())
   comandoSoft = "SELECT nme_software, ver_software FROM tb_software WHERE cod_tipo=%s ORDER BY nme_software;"

   arv = ""
   for [idt, nome] in cs:
       arv += ", [{v:'tipo_" + str(idt) + "', f:'" + nome + "'}, 'tipos', 'Tipo de Software: " + nome + "']"
       mysqlSoft = bd.SQL("root", "uniceub", "test")
       csSoft = mysqlSoft.consultar(comandoSoft, [idt])
       for [soft, versao] in csSoft:
           arv += " ,['{}', 'tipo_{}', '{} - {}']\n".format(soft, str(idt), soft, versao)

       csSoft.close()
   cs.close()
   return render_template('org.html', arvore=arv)

app.run(debug=True)