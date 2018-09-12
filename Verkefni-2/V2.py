#Sigursteinn Óli Þorsteinsson
#05/09/18
#Verkefni 2

from bottle import *

@route("/")
def index():
    return """
    <h1> Verkefni 2 </h1>
    <a href="/a">Liður A</a> - 
    <a href="/b">Liður B</a>
    """

@route("/a")
def a():
    return """
    <h1> Verkefni 2 - A </h1>
    <a href="/">Forsíða</a>
    <a href="/sida/1">Síða 1</a>
    <a href="/sida/2">Síða 2</a>
    <a href="/sida/3">Síða 3</a>   
    """

@route("/sida/<id>")
def page(id):
    if id == "1":
        return "Þetta er síða 1 <br><a href='/a'>Til baka</a>"
    elif id == "2":
        return "Þetta er síða 2 <br><a href='/a'>Til baka</a>"
    elif id == "3":
        return "Þetta er síða 3 <br><a href='/a'>Til baka</a>"

    elif id == "A":
        return "Þetta er síða 1 <br><a href='/b'>Til baka</a>"
    elif id == "B":
        return "Þetta er síða 2 <br><a href='/b'>Til baka</a>"
    elif id == "C":
        return "Þetta er síða 3 <br><a href='/b'>Til baka</a>"
    elif id == "D":
        return "Þetta er síða 3 <br><a href='/b'>Til baka</a>"
    else:
        return "<h1 style = color:red>Þessi síða finnst ekki</h1>"

@route("/b")
def b():
    return """
    <h1> Verkefni 2 - B </h1>
    <a href="/sida/?bokstafur=A"><img src="myndir/crown.png"></a>
    <a href="/sida/?bokstafur=B"><img src="myndir/pringles.png"></a>
    <a href="/sida/?bokstafur=C"><img src="myndir/smile.png"></a>
    <a href="/sida/?bokstafur=D"><img src="myndir/skull.png"></a>
    """

@route("sida2")
def page():
    l = request.query.bokstafur
    if l == "A":
        return "<h1>sigursteinn</h1>"
    if l == "B":
        return "<h1>sigursteinn</h1>"
    if l == "C":
        return "<h1>sigursteinn</h1>"
    if l == "D":
        return "<h1>sigursteinn</h1>"


@route("/myndir/<skra>")
def static_skrar(skra):
    return static_file(skra, root="myndir")



@error(404)
def villa(error):
    return "<h1 style = color:red>Þessi síða finnst ekki</h1>"









run(host="localhost", port =8080, reloader=True, debug=True)
