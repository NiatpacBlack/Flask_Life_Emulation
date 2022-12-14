# Flask_Life_Emulation
Учебный проект курса по Flask. [Игра "Жизнь".](https://ru.wikipedia.org/wiki/%D0%98%D0%B3%D1%80%D0%B0_%C2%AB%D0%96%D0%B8%D0%B7%D0%BD%D1%8C%C2%BB) Проект написан на основе [клеточного автомата.](https://ru.wikipedia.org/wiki/%D0%9A%D0%BB%D0%B5%D1%82%D0%BE%D1%87%D0%BD%D1%8B%D0%B9_%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82)

На заданном клеточном поле случайно зарождается жизнь в виде зеленого квадрата, после чего клетки могут размножаться и умирать (становиться красным квадратом).
Мы можем только наблюдать за развитием клеток или вручную переключать поколения.

![image](https://user-images.githubusercontent.com/84034483/189501231-a4558776-c509-4e3d-a364-9df3b94b086c.png)

## Запуск проекта
   - Устанавливаем зависимости из requirements.txt: `pip install -r requirements.txt` Для Unix-систем вместо `pip` потребуется `pip3`.
   - вводим команду: `flask run`
   - альтернативный вариант для Unix-систем - установите gunicorn `pip3 install gunicorn` и введите команду `gunicorn --bind 127.0.0.1:5000 app:app`, в данном случае приложение будет доступно в локальной сети.
   - альтернативный вариант для Windows - установите waitress `pip install waitress` и введите команду `waitress-serve --listen=127.0.0.1:5000 app:app`

