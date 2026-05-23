# Свидетелства

Веб апликација за пополнување и печатење на свидетелства (Образец бр. 20) за средни училишта во Република Северна Македонија.

---

## Барања

| Софтвер | Верзија |
|---------|---------|
| Python  | 3.10 или понова |
| pip     | (доаѓа со Python) |

Нема потреба од интернет конекција по инсталацијата. Базата е SQLite — не треба посебен сервер за база.

---

## Инсталација на Windows

### 1. Инсталирај Python

1. Оди на [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Преземи ја најновата верзија за Windows (Python 3.x.x)
3. Стартувај го инсталерот
4. **ВАЖНО:** Стави штиклирање на „Add Python to PATH" пред да кликнеш Install

### 2. Преземи ја апликацијата

Копирај ја папката `svidetelstva` на PC-то (на пример на `C:\Svidetelstva\`).

Структурата треба да изгледа вака:
```
C:\Svidetelstva\
└── svidetelstva\
    ├── app.py
    ├── database.py
    ├── requirements.txt
    ├── templates\
    └── static\
```

### 3. Отвори Command Prompt во папката

Во File Explorer оди во папката `C:\Svidetelstva\svidetelstva\`, потоа во address bar напиши `cmd` и притисни Enter.

### 4. Инсталирај зависности

```
pip install -r requirements.txt
```

### 5. Стартувај ја апликацијата

```
python app.py
```

Ќе видиш порака слична на:
```
* Running on http://0.0.0.0:5000
* Running on http://192.168.x.x:5000
```

### 6. Отвори во пребарувач

На истиот PC: [http://localhost:5000](http://localhost:5000)

На останатите PC-а во мрежата: `http://192.168.x.x:5000` (IP адресата од пораката горе)

### Проблем со Firewall на Windows?

Ако другите PC-а не можат да се поврзат, дозволи го пристапот:

1. Отвори **Windows Defender Firewall**
2. Кликни „Allow an app through firewall"
3. Кликни „Allow another app..." → пронајди го `python.exe`
4. Стави штиклирање на „Private" и кликни OK

Или преку Command Prompt (со администраторски права):
```
netsh advfirewall firewall add rule name="Svidetelstva" dir=in action=allow protocol=TCP localport=5000
```

---

## Инсталација на Linux

### 1. Инсталирај Python (ако не е инсталиран)

**Ubuntu / Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**Fedora / RHEL:**
```bash
sudo dnf install python3 python3-pip
```

**Arch Linux:**
```bash
sudo pacman -S python python-pip
```

### 2. Оди во папката на апликацијата

```bash
cd /патека/до/svidetelstva
```

### 3. Инсталирај зависности

```bash
pip3 install -r requirements.txt
```

### 4. Стартувај ја апликацијата

```bash
python3 app.py
```

### 5. Отвори во пребарувач

На истиот PC: [http://localhost:5000](http://localhost:5000)

На останатите PC-а: `http://192.168.x.x:5000`

---

## Автоматско стартување при вклучување на PC (Windows)

Ако сакаш апликацијата да се стартува автоматски:

1. Создади фајл `start_svidetelstva.bat` со следната содржина:
```bat
@echo off
cd C:\Svidetelstva\svidetelstva
python app.py
```

2. Стави ја оваа `.bat` датотека во:
`C:\Users\[твоето ime]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

---

## Прва употреба

При прво стартување автоматски се:
- Креира базата (`svidetelstva.db`)
- Додава администраторски корисник

**Стандардни податоци за најава:**

| Поле     | Вредност  |
|----------|-----------|
| Корисник | `admin`   |
| Лозинка  | `admin123` |

**Веднаш по најавата смени ја лозинката преку Администрација → Корисници.**

---

## Поставки по инсталација

Пред да почнеш со внесување свидетелства, постави ги основните податоци:

1. Одлогирај → Администрација → **Поставки**
2. Внеси:
   - Назив на средното училиште
   - Општина/Град
   - Акт број за верификација
   - Датум на акт
   - Издаден од

---

## Структура на проектот

```
svidetelstva/
├── app.py              # Flask апликација и рути
├── database.py         # База и SQL функции
├── requirements.txt    # Python зависности
├── svidetelstva.db     # SQLite база (создава се автоматски)
├── templates/          # HTML шаблони
│   ├── admin/
│   ├── base.html
│   ├── certificate_form.html
│   ├── print_preview.html
│   └── ...
└── static/
    ├── img/            # Скенирани свидетелства (позадина за печат)
    └── download/       # Excel шаблони за увоз
```

---

## Увоз на ученици и предмети

Во папката `static/download/` се наоѓаат CSV шаблони:

- `uchenici_template.csv` — шаблон за увоз на ученици
- `predmeti_template.csv` — шаблон за увоз на предмети

Пополни ги во Excel и зачувај ги. Увозот се врши преку Администрација.

---

## Пристап од мрежата

Апликацијата работи на **порт 5000**. Сите PC-а во училишната мрежа можат да пристапат преку пребарувач без инсталација на ништо.

```
http://[IP на серверскиот PC]:5000
```

За да го дознаеш IP-то на серверскиот PC:
- **Windows:** отвори cmd → напиши `ipconfig` → погледај „IPv4 Address"
- **Linux:** во терминал напиши `ip a` или `hostname -I`
