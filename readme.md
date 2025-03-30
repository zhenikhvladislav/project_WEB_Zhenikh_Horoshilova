# ResumeBuilder — Веб-приложение для создания резюме

## О проекте

**ResumeBuilder** — это веб-приложение, позволяющее пользователям быстро и удобно создать резюме с нуля, выбрать шаблон и экспортировать результат в PDF.

### Авторы проекта
- **Тимлид:** Жених Владислав
- **Разработчик:** Хорошилова Аксинья
- **Учитель:** Анатольев Алексей Владимирович

### Количество строк кода
>  Примерно 500 строк

### Техническое задание
  [Техническое задание](materials/technical_specification.md)

---

## Установка библиотек и запуск проекта

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/resume-builder.git
cd resume-builder
```

2. Установите зависимости:
```bash
npm install      # frontend (client/)
pip install -r requirements.txt  # backend (Flask)
```

3. Запустите frontend:
```bash
npm start
```

4. Запустите backend:
```bash
cd backend
python app.py
```

---

## Администрирование проекта

| Действия пользователя               | Действия администратора / системы         |
|---------------------------------------------|------------------------------------------------------|
| Заходит на сайт                          | Отвечает сервер, показывает главную страницу |
| Регистрируется / входит            | Валидация данных, сохранение в БД / localStorage |
| Выбирает шаблон                     | Отправка UI шаблона пользователю         |
| Вводит данные                          | Сохранение в базу или в localStorage        |
| Экспортирует в PDF                    | jsPDF/html2canvas формируют файл PDF      |

---

## Управление для пользователя

### Вход и регистрация

- Доступны способы:
  - E-mail + пароль
  - OAuth: Google, GitHub

- Возможности после входа:
  - Создание и редактирование резюме
  - Выбор шаблона
  - Загрузка фото
  - Экспорт PDF

### Скриншоты:

1. Регистрация
![registration](./materials/screenshots/registration.png)

2. Шаблоны
![templates](./materials/screenshots/templates.png)

3. Редактор
![editor](./materials/screenshots/editor.png)

4. Экспорт
![pdf-preview](./materials/screenshots/pdf_preview.png)

---

## Технологии
- **Frontend:** React, TailwindCSS, Redux
- **Backend:** Flask / Express
- **База данных:** Firebase / localStorage
- **Генерация PDF:** jsPDF, html2canvas
- **Дизайн:** минимализм, адаптивность

