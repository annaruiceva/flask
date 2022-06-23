from flask import Flask, render_template

about = '''Оставили бабушке рожки да ножки. 
Из детской песенки неизвестного автора, которая впервые появилась в русской литературе, когда писатель И. С. Тургенев включил ее в текст своей комедии «Месяц в деревне» (1855). '''

menu_list = ["картошка", "салат", "лук"]
promo = '''Минскреклама
4,0
(122) · Рекламное агентство
Работает более 5 лет. · ул. Ивановская 43а · 8 017 290-57-37
Открыто ⋅ Закроется в 18:00

Услуги: Реклама на бигбордах
Сайт
Маршрут
АДС-24 | Наружная реклама | Широкоформатная печать
4,8
(41) · Рекламное агентство
Работает более 10 лет. · ул. Олешева д.5, 206 · 8 029 662-28-58
Открыто ⋅ Закроется в 18:00
Сайт
Маршрут
Qmedia — контекстная реклама, SEO-продвижение сайтов, разработка
4,5
(50) · Рекламное агентство
Работает более 15 лет. · ул. Старовиленская 100 · 8 029 335-23-23
Открыто ⋅ Закроется в 18:00
Обслуживание на месте·
Онлайн-приемы'''

app = Flask(__name__,
            template_folder='templates',
            static_folder='static',
            )

@app.route('/')
def main():
    return render_template("index2.html",
                           list=menu_list,
                           site_name="Рожки да ножки",
                           about=about,
                           promo = promo,
                           bye="Заходите еще!!!")


if __name__ == '__main__':
    app.run(port="8000")
