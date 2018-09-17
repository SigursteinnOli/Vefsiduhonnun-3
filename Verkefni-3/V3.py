#Sigursteinn Óli Þorsteinsson
#10/09/18
#Verkefni 3

from bottle import *

@route("/")
def index():
    return """
    <h1> Verkefni 3 </h1>
    <a href="/a">Liður A</a> - 
    <a href="/b">Liður B</a>
    """
@route("/a")
def index():
    return template("tempA.tpl")

@route("/sida/<kt>")
def page(kt):
    return template("temp_kt.tpl",kt=kt)

@route("/static/<skra>")
def static_skra(skra):
    return static_file(skra, root="./static")



frettir = [["Irma veldur usla á Flórída", "Það er bara ... vesen á Irmu í Flórída.  Milljónir manna hafa þurft að yfirgefa heimili sin vegna yfirvofandi eyðileggingar Irmu...", "irma.jpg", "dsg@frettir.is"],
           ["Veiðin er dræm þetta haustið", "Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið...", "veidi.png", "est@frettir.is"],
           ["Ólafía stendur sig vel", "Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili...", "golf.jpeg", "htg@frettir.is"],
           ["Ísland dottið úr leik", "Íslenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli.  Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum..", "karfa.jpeg", "dsg@frettir.is"]]

@route("/b")
def index():
    return template("index.tpl", frettir = frettir)

@route("/frett/<id:int>")
def index(id):
    return template("frett.tpl", frett = frettir[id], nr = id)



@error(404)
def villa(error):
    return "<h1 style = color:red>Þessi síða finnst ekki</h1>"


run(host="localhost", port =8080, reloader=True, debug=True)



