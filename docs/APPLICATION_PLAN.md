# План програмного застосунку

## 1. Призначення

Програмний застосунок є демонстраційним інтерфейсом інтелектуальної системи
прогнозування добових енергетичних витрат користувача на основі даних
фітнес-трекера.

Застосунок використовує попередньо навчену модель машинного навчання та
дозволяє користувачу отримати прогноз, переглянути історичні дані,
характеристики активності та пояснення результатів роботи моделі.

Реалізація застосунку виконується у вигляді інтерактивного dashboard на базі:

- Python;
- Google Colab;
- Voilà;
- Jupyter Widgets;
- підготовлених ML-артефактів.

---

# 2. Архітектура застосунку

```
Final ML Artifacts

        │

        ▼

Random Forest Model
(random_forest_final.pkl)

        │

        ▼

Model Metadata
(model_metadata.json)

        │

        ▼

Prediction Engine

        │

        ▼

Voilà Dashboard

        │

        ▼

User Interface
```

---

# 3. Основний сценарій роботи

1. Користувач відкриває dashboard застосунку.

2. Система завантажує необхідні фінальні артефакти:

- навчену модель;
- список ознак;
- результати прогнозування;
- історичні дані;
- метадані моделі.

3. Користувач обирає:

- ID користувача;
- дату прогнозування.

4. Система:

- знаходить доступні історичні дані;
- формує часові ознаки;
- готує вхідний вектор для моделі.

5. Модель машинного навчання формує прогноз Calories на наступний день.

6. Результат відображається в інтерфейсі.

7. Користувач може переглянути:

- прогнозоване значення;
- фактичні значення;
- історію активності;
- важливість ознак;
- пояснення прогнозу.

---

# 4. Основний екран

Основний інтерфейс містить:

## Вибір параметрів

```
ПРОГНОЗУВАННЯ ДОБОВИХ ЕНЕРГОВИТРАТ


Користувач:

[ User ID ▼ ]


Дата прогнозування:

[ YYYY-MM-DD ▼ ]


[ Сформувати прогноз ]
```

---

# 5. Блок прогнозування

Відображається результат роботи моделі:

```
ПРОГНОЗ


Очікувані Calories наступного дня:


        XXXX kcal


Модель:

Random Forest
```

Додатково можуть відображатися:

```
MAE:
XXX kcal


RMSE:
XXX kcal
```

---

# 6. Блок останньої активності

Відображення основних показників користувача:

```
ОСТАННЯ АКТИВНІСТЬ


Steps

Distance

Active Minutes

Sedentary Minutes

Calories
```

---

# 7. Історія прогнозів

Dashboard повинен містити графічне представлення часової історії:

```
ІСТОРІЯ


Actual Calories

vs

Predicted Calories
```

Відображаються:

- фактичні значення Calories;
- прогнозовані значення;
- часовий тренд.

---

# 8. Аналіз моделі

Для пояснення результатів використовується Explainable AI.

Підтримуються:

- Feature Importance;
- SHAP analysis.

Приклад:

```
Найважливіші ознаки:


• Calories попереднього дня

• TotalSteps

• ActiveMinutes

• Lag features

• Rolling statistics
```

---

# 9. Інформація про модель

Dashboard повинен відображати інформацію про використану модель:

```
MODEL INFORMATION


Algorithm:

Random Forest


Features:

65 engineered features


Temporal features:

- lag 1
- lag 2
- lag 3
- lag 7


Rolling statistics:

- mean
- std
```

---

# 10. Структура реалізації

```
0014_VOILA.ipynb

    │
    ├── Runtime configuration
    │
    ├── Load final artifacts
    │
    ├── Model loader
    │
    ├── Prediction functions
    │
    ├── SHAP analysis
    │
    └── Interactive dashboard


0015x_VOILA_LAUNCHER.ipynb

    │
    ├── Environment preparation
    │
    ├── Voilà startup
    │
    ├── Runtime diagnostics
    │
    └── Application launch
```

---

# 11. Поточний статус

## Completed

- [x] Final ML pipeline
- [x] Final Random Forest model
- [x] Model artifact export
- [x] Prediction results generation
- [x] Metadata generation
- [x] Initial Voilà application
- [x] Interactive widgets integration


## In progress

- [ ] Finalize Voilà launcher
- [ ] Improve dashboard layout
- [ ] Validate widget rendering
- [ ] Add final interface polishing
- [ ] Prepare final demonstration version


## Future improvements

- [ ] Additional model comparison interface
- [ ] Extended user analytics
- [ ] Export prediction reports
- [ ] Additional visualization modules
