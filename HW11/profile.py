from flask import Flask


app = Flask(__name__)


@app.route('/',)
def page_index():

    page_content = """ 
    <h1>Тарзан</h1>
    
    <img src="https://media.istockphoto.com/vectors/tarzan-vector-id165678959" width="300" height="200">
    <br>
    <p><strong>Тарзан</strong> (англ. Tarzan) — персонаж, созданный писателем <ins>Эдгаром Райсом Берроузом</ins>.</p>
    <p>И впервые появившийся в книге <em>«Тарзан. Приёмыш обезьяны»</em></p>
    
    <a href="https://ru.wikipedia.org/wiki/%D0%A2%D0%B0%D1%80%D0%B7%D0%B0%D0%BD">Полная информация по ссылке в википедия</a>
    <br>
    <br/>
    <p> Просьба не путать с этим <del>Тарзаном</del> </p>
    <img src="https://cdnn21.img.ria.ru/images/07e4/05/16/1571817587_0:0:2048:3433_1440x900_80_1_1_1e9054946e01f86d9e8f167e45f5b6c6.jpg.webp?source-sid=rian_photo" width="200" height="200">
    
    """
    return page_content


app.run(host='127.0.0.2', port=80)