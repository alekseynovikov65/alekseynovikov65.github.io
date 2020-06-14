#что такое твой сайт
#http://127.0.0.1:5000/   - адрес сайта
#у сайта есть странички
#у каждой странички тоже должен быть адрес
#и этот адрес будет состоят из адреса сайта + слеш + что еще. Например Index.html, "/библиотека/романы/войнаимир.html"
#
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')      #мы открываем сайт http://127.0.0.1:5000/   
def go():
    filename = 'programm.csv'
    with open(filename, 'w') as file_object: #открывает файл programm.csv, каким образом? если файл существует то стирает и создает новый
        file_object.write('name') #пишем в файл  name
        file_object.write(',')#пишем в файл  ,
        file_object.write('email')
        file_object.write(',')
        file_object.write('answer')
        file_object.write("\n")#пишем в файл перенос строки
    return render_template('1.html') #отображаем html документ 1.html
# что мы имеем после открытия сайта, у нас создан файл program.csv и в нем есть строка "name,email,answer"


#-----
#сайт в ожидании ввода
#мы заполнили форму, нажали на кнопку отправить (тег input type="submit")
#наша форма отправляет данные методом ПОСТ на УРЛ адрес в атрибуте ACTION (<form action='/answer') методом <form method='POST'>
# в соответствии с этим адресом(form action='/answer') срабатывает роут @app.route('/answer', methods=['POST']
# 
@app.route('/answer', methods=['POST']) 
def nn():
    name = request.form['name']
    email = request.form['email']
    answer = request.form['message'] 
    filename = 'programm.csv'

    with open(filename, 'a') as file_object:
        file_object.write(name)
        file_object.write(',')
        file_object.write(email)
        file_object.write(',')
        file_object.write(answer)
        file_object.write("\n")

    return render_template('1.html')


if __name__ == '__main__':
    app.run(debug=True)

#<http request GET
#URL http://127.0.0.1:5000/?name=Kate&Age=20&Address=Moskva
#<http request>
#
#<http request POST>
#URL http://127.0.0.1:5000/answer
#DATA 
#    <name/> = Kate
#    <Age/> 20
#    <Address/> Moskva
#    
#<http request>
